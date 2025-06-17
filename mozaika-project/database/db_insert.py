import pandas as pd

materials_df = pd.read_excel('../resources/Materials_import.xlsx', sheet_name=None) #None - чтобы загрузил все листы
loss = pd.read_excel('../resources/Material_type_import.xlsx')
suppliers_info_df = pd.read_excel('../resources/Suppliers_import.xlsx', sheet_name=None)
material_suppliers_df = pd.read_excel('../resources/Material_suppliers_import.xlsx', sheet_name=None)
product_types = pd.read_excel('../resources/Product_type_import.xlsx')


def insert(cursor):
    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ material_types ---
    def insert_material_types():
        # выбор листа "idtypematerials"
        idtypematerial = materials_df['idtypematerial']

        # проходимся по колонкам idtypematerial и записываем значения в переменные
        for i in range(len(idtypematerial)):
            id = int(idtypematerial.iloc[i, 0])
            material_type = idtypematerial.iloc[i, 1]

            # ищем совпадение по типу материала т.к. id в таблицах не совпадают
            match = loss[loss['Тип материала'] == material_type]

            if not match.empty:
                loss_percentage = match.iloc[0, 2]

                cursor.execute('''
                INSERT OR IGNORE INTO material_types
                ( id, material_type, loss_percentage )
                VALUES (?, ?, ?)
                ''', (id, material_type, loss_percentage))
            else:
                print (f'не найдено значение для {material_type}')


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ materials_insert ---
    def insert_material_names():
        idmaterialnames = materials_df['idnamematerial']

        for i in range(len(idmaterialnames)):
            id = int(idmaterialnames.iloc[i, 0])
            material_name = idmaterialnames.iloc[i, 1]

            cursor.execute('''
            INSERT OR IGNORE INTO material_names 
            ( id, material_name )
            VALUES (?, ?)
            ''', (id, material_name))


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ materials ---
    def insert_materials():
        materials = materials_df['Materials_import']

        for i in range(len(materials)):
            id = int(materials.iloc[i, 0])
            material_type_id = int(materials.iloc[i, 1])
            material_name_id = int(materials.iloc[i, 2])
            price = materials.iloc[i, 5]
            quantity = int(materials.iloc[i, 6])
            min_quantity = int(materials.iloc[i, 7])
            pack_size = int(materials.iloc[i, 8])
            unit = materials.iloc[i, 9]

            cursor.execute('''
            INSERT OR IGNORE INTO materials
            ( id, material_type_id, material_name_id, price, quantity, min_quantity, pack_size, unit )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id, material_type_id, material_name_id, price, quantity, min_quantity, pack_size, unit))


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ company_types ---
    def insert_company_types():
        company_types = suppliers_info_df['idpost']

        for i in range(len(company_types)):
            id = int(company_types.iloc[i, 0])
            company_type = company_types.iloc[i, 1]

            cursor.execute('''
            INSERT OR IGNORE INTO company_types
            ( id, company_type )
            VALUES (?, ?)
            ''', (id, company_type))


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ company_names ---
    def insert_company_names():
        company_names = suppliers_info_df['idnamepost']

        for i in range(len(company_names)):
            id = int(company_names.iloc[i, 0])
            company_name = company_names.iloc[i, 1]

            cursor.execute('''
            INSERT OR IGNORE INTO company_names
            ( id, company_name )
            VALUES (?, ?)
            ''', (id, company_name))


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ suppliers_info ---
    def insert_suppliers_info():
        suppliers_info = suppliers_info_df['Suppliers_import']

        for i in range(len(suppliers_info)):
            id = int(suppliers_info.iloc[i, 0])
            company_type_id = int(suppliers_info.iloc[i, 1])
            company_name_id = int(suppliers_info.iloc[i, 2])
            INN = int(suppliers_info.iloc[i, 5])
            rating = int(suppliers_info.iloc[i, 6])
            start_date = str(suppliers_info.iloc[i, 7].strftime('%Y-%m-%d'))

            cursor.execute('''
            INSERT OR IGNORE INTO suppliers_info
            ( id, company_type_id, company_name_id, ИНН, rating, start_date )
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (id, company_type_id, company_name_id, INN, rating, start_date))


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ material_suppliers ---
    def insert_material_suppliers():
        material_suppliers = material_suppliers_df['Material_suppliers_import']

        for i in range(len(material_suppliers)):
            id = int(material_suppliers.iloc[i, 0])
            material_name_id = int(material_suppliers.iloc[i, 1])
            company_name_id = int(material_suppliers.iloc[i, 3])

            cursor.execute('''
            INSERT OR IGNORE INTO material_suppliers
            ( id, material_name_id, company_name_id )
            VALUES (?, ?, ?)
            ''', (id, material_name_id, company_name_id))


    # --- ЗАПОЛНЕНИЕ ТАБЛИЦЫ product_types ---
    def insert_product_types():
        for i in range(len(product_types)):
            id = int(product_types.iloc[i, 0])
            product_type = product_types.iloc[i, 1]
            coefficient = product_types.iloc[i, 2]

            cursor.execute('''
            INSERT OR IGNORE INTO product_types
            ( id, product_type, coefficient )
            VALUES (?, ?, ?)
            ''', (id, product_type, coefficient))


    insert_material_types()
    insert_material_names()
    insert_materials()
    insert_company_types()
    insert_company_names()
    insert_suppliers_info()
    insert_material_suppliers()
    insert_product_types()

