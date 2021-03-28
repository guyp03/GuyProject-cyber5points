import sqlite3
my_table=sqlite3.connect('acounts.db')
my_table_c=my_table.cursor()
my_table_c.execute("""CREATE TABLE acountsTable (
              userName text,
              password text         
              )""")
my_table.commit()
my_table.close()

