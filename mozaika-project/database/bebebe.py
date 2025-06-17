import sqlite3

# подключаешь к файлу
connection = sqlite3.connect('database.db')

# штука чтобы выполнять запросы
cursor = connection.cursor()

# выполняешь запросы с помощью cursor.execute
# в (''' ''') пишешь запрос

# пример
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS material_types (
#     id INTEGER PRIMARY KEY,
#     material_type TEXT NOT NULL UNIQUE,
#     material_name_id INTEGER NOT NULL,
#     price FLOAT NOT NULL,
#     FOREIGN KEY(material_name_id) REFERENCES material_names(id)
# )
# ''')

# СОЗДАТЬ ТАБЛИЦУ ЕСЛИ ТАКОЙ ЕЩЕ НЕ СУЩЕСТВУЕТ название_таблицы (
# название_колонки ТИП_ДАННЫХ ДОПОЛНИТЕЛЬНАЯ_ХУЙНЯ
# )

# -- ТИПЫ ДАННЫХ которые мне пригодились в задании --
# INTEGER - целое число
# FLOAT - дробное число (с запятой)
# TEXT - текст

# -- ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ ДЛЯ ПОЛЕЙ --
# PRIMARY KEY - первичный ключ
# FOREIGN KEY - внешний
# NOT NULL - поле не должно быть пустым
# UNIQUE - значение не должно повторяться

# -- СВЯЗЬ ОДНОЙ ТАБЛИЦЫ С ДРУГИМИ ТАБЛИЦАМИ --
# FOREIGN KEY(название_твоей_колонки) REFERENCES название_другой_таблицы(название_колонки_из_другой_таблицы)
# типа данные связаны

# каждый запрос пишешь в новом cursor.execute

cursor.execute('''
CREATE TABLE IF NOT EXISTS dota_ranks (
    id INTEGER PRIMARY KEY,
    rank TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dota_players (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dota_rank_id INTEGER NOT NULL,
    FOREIGN KEY (dota_rank_id) REFERENCES dota_ranks(id)
)
''')

# завершаешь работу с склайтом
connection.commit()
connection.close()