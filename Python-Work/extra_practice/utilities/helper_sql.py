import psycopg2
import logging
from db_module_psql import db_config


# LOGGER
def init_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Start of program and logger')
    print('just in case kkkkkk.')


def psql_connection_test():
    # Connect to the PostgreSQL database server
    conn = None

    try:
        # Connect to the PostgreSQL server
        logging.info('Connection to the PostgreSQL database...')
        conn = psycopg2.connect(host=db_config.host, database=db_config.database,
                                user=db_config.user, password=db_config.password, port=db_config.port)

        # Create a cursor
        cur = conn.cursor()

        # Execute a Statement
        logging.info('PostgreSQL database version: ')
        cur.execute('SELECT version()')

        # display yhe PostgreSQL database server version
        db_version = cur.fetchone()
        logging.info(db_version)

        # close the communication with the
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        if conn is not None:
            conn.close()
            logging.info('Database connection closed')


def psql_connection():
    # Connect to the PostgreSQL database server
    conn = None
    try:
        # connect to the PostgreSQL server
        logging.info('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host='localhost', database="playground", user="postgres", password='root', port=5432)

        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)


def create_table(psql_conn):
    # create tables in the PostgreSQL database
    q_create_table = """
        CREATE TABLE IF NOT EXISTS members (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            discord_name VARCHAR(255) NOT NULL,
            reason_to_code VARCHAR(255) NOT NULL,
            addicted_to VARCHAR(255) NOT NULL)"""

    try:
        cur = psql_conn.cursor()
        # execute each query from the commands tuple
        cur.execute(q_create_table)
        logging.info(f'Executed query: {q_create_table}')

        # close communication with PostgreSQL
        cur.close()

        # commit the changes
        psql_conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)


def insert_member(psql_conn, member):
    # Insert a new member into the members table
    q_insert_member = """
            INSERT INTO members(name, discord_name, reason_to_code, addicted_to) VALUES(%s,%s,%s,%s)
    """

    try:
        cur = psql_conn.cursor()

        cur.execute(q_insert_member, (member['name'], member['discord_name'],
                    member['reason_to_code'], member['addicted_to']))

        # commit the changes
        psql_conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f'Error in <insert_member> function {error}')

    finally:
        # close communication with PostgreSQL
        cur.close()


def select_all_data(connection):
    try:
        cursor = connection.cursor()

        # Ejecuta una consulta SELECT
        cursor.execute("SELECT * FROM members")

        # Verifica si hay resultados antes de llamar a fetchall()
        if cursor.rowcount > 0:
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            print("No hay resultados para mostrar.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error: {error}')

    finally:
        # Cierra el cursor
        if cursor:
            cursor.close()
