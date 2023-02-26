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
            """FUNCTIONS"""

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
                    insert_data_sql = f"INSERT INTO `{table_name}`{columns} VALUES {values};" # sql request
                    cursor.execute(insert_data_sql) # send request
                    connection.commit() # commit request
                    print(f"insert data '{table_name}' successfully✅")

            def update_data(table_name: str, id: int, values: str):
                """Function to update data

                Args:
                    table_name (str): Name of the table,
                    id (int): Id of the row,
                    values (str): Values of the row.
                """                
                with connection.cursor() as cursor: # connection.cursor => cursor
                    update_data_sql = f"UPDATE `{table_name}` SET {values} WHERE id={id};" # sql request
                    cursor.execute(update_data_sql) # send request
                    connection.commit() # commit request
                    print(f"update data '{table_name}' successfully✅")
            
            def delete_data(table_name: str, id: str):
                """Function to delete data

                Args:
                    table_name (str): Name of the table,
                    id (int): Id of the row.
                """                
                with connection.cursor() as cursor: # connection.cursor => cursor
                    delete_data_sql = f"DELETE FROM `{table_name}` WHERE id={id};" # sql request
                    cursor.execute(delete_data_sql) # send request
                    connection.commit() # commit request
                    print(f"delete data '{table_name}' successfully✅")

            """INTERPRETER"""

            while True:
                command = input('please, input command (help): ') # input
                find_command = command.split() # find commands

                match find_command[0]: # interpreter
                    case 'help':
                        print("""Commands:
                                 create_table - Command to create table,
                                 view_table - Command to view table,
                                 drop_table - Command to drop table,
                                 insert_data - Command to insert data,
                                 update_data - Command to update data,
                                 delete_data - Command to delete data,
                                 exit - Command to exit terminal.

                                 (command) info - info about command
                        """)
                    case 'create_table':
                        find_params = find_command.split(" ", 2)
                        if find_params[1] == 'info':
                            print('create_table => params: table_name, columns💡')
                        else:
                            create_table(find_params[1], find_params[2])
                    case 'view_table':
                        find_params = find_command.split(" ", 1)
                        if find_params[1] == 'info':
                            print('view_table => params: table_name💡')
                        else:
                            view_table(find_params[1])
                    case 'drop_table':
                        find_params = find_command.split(" ", 1)
                        if find_params[1] == 'info':
                            print('drop_table => params: table_name💡')
                        else:
                            drop_table(find_params[1])
                    case 'insert_data':
                        find_params = find_command.split(" ", 3)
                        if find_params[1] == 'info':
                            print('insert_data => params: table_name, columns, data💡')
                        else:
                            insert_data(find_params[1], find_params[2], find_params[3])
                    case 'update_data':
                        find_params = find_command.split(" ", 3)
                        if find_params[1] == 'info':
                            print('updata_data => params: table_name, id, data💡')
                        else:
                            update_data(find_params[1], find_params[2], find_params[3])
                    case 'delete_data':
                        find_params = find_command.split(" ", 2)
                        if find_params[1] == 'info':
                            print('delete_data => params: table_name, id💡')
                        else:
                            insert_data(find_params[1], find_params[2])
                    case 'exit':
                        break
                    case _:
                        print(f'invalid command: {find_command[0]}❌')
        finally:
            print('connection closed⛔')
            connection.close()  # close connection
    except Exception as e:
        print(f'failed to connect: {e}❌')