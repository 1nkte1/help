import sqlite3
# import pandas as pd

connection = sqlite3.connect('materials.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS material_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_type TEXT NOT NULL UNIQUE,
    loss_percentage FLOAT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS material_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_name TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_type_id INTEGER NOT NULL,
    material_name_id INTEGER NOT NULL,
    price FLOAT NOT NULL,
    quantity INTEGER,
    min_quantity INTEGER,
    pack_size INTEGER,
    unit TEXT,
    FOREIGN KEY(material_type_id) REFERENCES material_types(id),
    FOREIGN KEY (material_name_id) REFERENCES material_names(id)
)    
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS company_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_type TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS company_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_type_id INTEGER NOT NULL,
    company_name_id INTEGER NOT NULL,
    ИНН INTEGER,
    rating INTEGER,
    start_date TEXT,
    FOREIGN KEY(company_type_id) REFERENCES company_types(id),
    FOREIGN KEY (company_name_id) REFERENCES company_names(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS material_suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    FOREIGN KEY(supplier_id) REFERENCES suppliers(id),
    FOREIGN KEY(material_id) REFERENCES materials(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_type TEXT NOT NULL UNIQUE,
    coefficient FLOAT NOT NULL
)
''')

print("yay")

connection.commit()
connection.close()