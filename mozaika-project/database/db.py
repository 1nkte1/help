import sqlite3
from db_create import *
from db_insert import insert

connection = sqlite3.connect('materials.db')
cursor = connection.cursor()

drop_all_tables(cursor)
# создание БД
create(cursor)
# импорт данных из таблиц excel в БД
insert(cursor)
print("все вставлено!")

connection.commit()
connection.close()

# cursor.execute('SELECT * FROM company_types')
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
