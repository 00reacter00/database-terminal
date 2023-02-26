import pymysql
from config import host, user, password, database

if __name__ == '__main__':
    print(f"""Profile: 
              > host: {host}
              > database: {database}
              > user: {user}
              > password: {len(password)}""")
    print('—' * 40)

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
        print('—' * 40)

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
                    cursor.execute(create_table_sql)  # send request
                    connection.commit() # commit request
                    print(f"create table '{table_name}' successfully✅")

            def view_table(table_name: str):
                """Function to view table

                Args:
                    table_name (str): Name of the table.
                """                
                with connection.cursor() as cursor: # connection.cursor => cursor
                    view_table_sql = f"SELECT * FROM `{table_name}`;" # sql request
                    cursor.execute(view_table_sql)  # send request
                    connection.commit() # commit request
                    data = cursor.fetchall() # fetch data from DB
                    for row in data: # table row output
                        print(row)

            def drop_table(table_name: str):
                """Function to drop table

                Args:
                    table_name (str): Name of the table.
                """                
                with connection.cursor() as cursor: # connection.cursor => cursor
                    drop_table_sql = f"DROP TABLE `{table_name}`;" # sql request
                    cursor.execute(drop_table_sql) # send request
                    connection.commit() # commit request
                    print(f"drop table '{table_name}' successfully✅")

            def insert_data(table_name: str, columns: str, values: str):
                """Function to insert data

                Args:
                    table_name (str): Name of the table,
                    columns (str): Columns of the table,
                    values (str): Values of the row.
                """                
                with connection.cursor() as cursor: # connection.cursor => cursor
                    drop_table_sql = f"INSERT INTO `{table_name}`{columns} VALUES {values};" # sql request
                    cursor.execute(drop_table_sql) # send request
                    connection.commit() # commit request
                    print(f"insert data '{table_name}' successfully✅")
        finally:
            connection.close()  # close connection
    except Exception as e:
        print(f'failed to connect: {e}❌')