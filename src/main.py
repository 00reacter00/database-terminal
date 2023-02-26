import pymysql
from config import host, user, password, database

if __name__ == '__main__':
    print(f"connecting to database '{database}'⏳")

    try:
        connection = pymysql.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )

        print('successfully connected✅')
        print('=' * 20)

        try:
            # command functions & interpreter
            def create_table(table_name: str, columns: str):
                """Function to create table

                Args:
                    table_name (str): Name of the table,
                    columns (str): Columns of the table.
                """                

                with connection.cursor() as cursor: # connection.cursor => cursor
                    create_table_sql = f"CREATE TABLE `{table_name}`{columns};" # sql request
                    cursor.execute(create_table_sql)  # create table
                    print('create table successfully✅')
        finally:
            connection.close()  # close connection
    except Exception as e:
        print(f'failed to connect: {e}⛔')