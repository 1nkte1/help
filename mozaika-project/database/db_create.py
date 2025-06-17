# ---СОЗДАНИЕ БАЗЫ ДАНЫХ---
def create(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS material_types (
        id INTEGER PRIMARY KEY,
        material_type TEXT NOT NULL UNIQUE,
        loss_percentage FLOAT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS material_names (
        id INTEGER PRIMARY KEY,
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
        id INTEGER PRIMARY KEY,
        company_type TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS company_names (
        id INTEGER PRIMARY KEY,
        company_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers_info (
        id INTEGER PRIMARY KEY,
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
        id INTEGER PRIMARY KEY,
        material_name_id INTEGER NOT NULL,
        company_name_id INTEGER NOT NULL,
        FOREIGN KEY(material_name_id) REFERENCES material_names(id),
        FOREIGN KEY(company_name_id) REFERENCES company_names(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_types (
        id INTEGER PRIMARY KEY,
        product_type TEXT NOT NULL UNIQUE,
        coefficient FLOAT NOT NULL
    )
    ''')

# --- УДАЛЕНИЕ ВСЕХ ТАБЛИЦ ---
def drop_all_tables(cursor):
    tables = [
        "material_types",
        "material_names",
        "materials",
        "company_types",
        "company_names",
        "suppliers_info",
        "material_suppliers",
        "product_types"
    ]
    for table in tables:
        cursor.execute(f'DROP TABLE IF EXISTS {table}')