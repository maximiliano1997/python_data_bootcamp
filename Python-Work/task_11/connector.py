import psycopg2
from db_modules import db_module_pro
# from db_modules.db_module_pro import create_table


if __name__ == '__main__':
    try:
        # Establecer la conexión a la base de datos
        with psycopg2.connect(
            host=db_module_pro.hostname,
            dbname=db_module_pro.database,
            user=db_module_pro.username,
            password=db_module_pro.password,
            port=db_module_pro.port_id
        ) as db_connector:

            # Crear un cursor para ejecutar comandos SQL
            with db_connector.cursor() as db_cursor:
                # Escribe tus consultas SQL aquí...
                create_table_script = db_module_pro.create_table()

                print("Generated SQL Script: ")
                print(create_table_script)

                # Ejecutar el script SQL
                db_cursor.execute(create_table_script)

                # Confirmar la transaccion
                db_connector.commit()

                # db_connector.close()

    except psycopg2.Error as e:
        # Manejar errores de psycopg2
        print(f"Error de psycopg2: {e}")

    # No necesitas cerrar explícitamente la conexión, ya que se maneja automáticamente con el bloque "with"
