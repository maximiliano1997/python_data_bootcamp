from utilities.helper_sql import init_logger, psql_connection_test, psql_connection, create_table, select_all_data
from utilities.get_data import get_selfdev_members

if __name__ == '__main__':
    init_logger()
    # psql_connection_test()
    conn = psql_connection()
    create_table(conn)
    get_selfdev_members(conn)
    select_all_data(conn)
