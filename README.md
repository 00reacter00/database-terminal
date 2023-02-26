# Terminal for connection database (v1.0)

Terminal for using MySQL database in Python.

With it, you can: __create/drop/view tables and add/delete/update data__.

# Setup
Create MySQL database.

Open the `config.py` and configure your database. You need to enter the host into the **'host'** variable, enter the username into the **'user'** variable, enter your password into the **'password'** variable and enter your database name into the **'database'** variable.

Run `main.py`

# Commands

After connecting to the database, you can use commands:

* **Create table** - `create_table`
* **Drop table** - `drop_table`
* **View table** - `select_table`
* **Update data** - `update_data`
* **Insert data** - `insert_data`
* **Delete data** - `delete_data`
