import csv
import json
import sqlite3
import glob
import os
import openpyxl
import psycopg2


def transform_to_csv(input_file, output_file):
    # Función para transformar el archivo de entrada a CSV
    if input_file.endswith('.json'):
        with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
            data = json.load(file_in)
            writer = csv.writer(file_out)
            writer.writerow(data[0].keys())  # Escribir encabezados
            for row in data:
                writer.writerow(row.values())
            print("Datos del archivo JSON escritos correctamente en el archivo CSV:", output_file)
    elif input_file.endswith('.xlsx'):
        data = openpyxl.load_workbook(input_file)
        sheet = data.active
        col = csv.writer(open(input_file[:-5] + "_output.csv", 'w', newline=""))

        for r in sheet.rows:
            if r[0].value is not None:
                col.writerow([cell.value for cell in r])
            else:
                continue
        print("Datos del archivo XLSX escritos correctamente en el archivo CSV:", output_file)
    elif input_file.endswith('.csv'):
        with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
            lines = file_in.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    file_out.write(line + '\n')
        print("Datos del archivo CSV copiados correctamente al nuevo archivo CSV:", output_file)
    elif input_file.endswith('.db'):
        transform_sqlite_to_csv(input_file, output_file)
    else:
        print("Formato de archivo no compatible:", input_file)


def transform_sqlite_to_csv(input_file, output_file):
    conn = sqlite3.connect(input_file)
    cursor = conn.cursor()

    # Obtener los nombres de las tablas en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        with open(output_file, "w", newline="") as csv_file:  # Utilizar el nombre de archivo de salida especificado
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])  # Escribir encabezados
            csv_writer.writerows(rows)  # Escribir filas de datos

    conn.close()


def main():
    current_dir = os.getcwd()

    file_patterns = ["*.csv", "*.json", "*.xlsx", "*.db"]

    input_files = []
    for pattern in file_patterns:
        input_files.extend(glob.glob(os.path.join(current_dir, pattern)))

    db_config = {  # Configuración de la conexión a la base de datos PostgreSQL
        'host': 'localhost',
        'database': 'test3',
        'user': 'user1',
        'password': 'user1'
    }

    for input_file in input_files:
        csv_output_file = os.path.splitext(input_file)[0] + '_output.csv'
        # Transformar el archivo de entrada a CSV
        print("Transformando archivo:", input_file)
        print("Generando archivo CSV de salida:", csv_output_file)
        transform_to_csv(input_file, csv_output_file)

        # Insertar datos en la base de datos desde el archivo CSV
        insert_into_database(csv_output_file, db_config)


def insert_into_database(csv_file, db_config):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header_row = next(reader)  # Obtener la fila de encabezado
        n_columns = len(header_row)
        table_name = os.path.splitext(os.path.basename(csv_file))[0]

        # Verificar si la tabla existe en la base de datos
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # Si la tabla no existe, crea una tabla temporal con las mismas columnas del CSV
            print(" \n")
            print(f"La tabla '{table_name}' no existe. Creando una nueva tabla...")
            columns_def = ", ".join([f'"{col}" VARCHAR(50) NOT NULL' for col in header_row])
            create_table_query = f"CREATE TABLE {table_name} ({columns_def})"
            print("Query de creación de tabla:", create_table_query)
            cursor.execute(create_table_query)
            print("Tabla creada exitosamente.")
        else:
            print(f"La tabla '{table_name}' ya existe.")

            # Si la tabla existe, obtén los nombres de las columnas de la tabla
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
            table_columns = [desc[0] for desc in cursor.description]

            # Verificar si los nombres de columna de la tabla coinciden con los del CSV
            if table_columns != header_row:
                print("Los nombres de las columnas en el archivo CSV no coinciden con los de la tabla existente.")
                return

        # Construir la parte de la consulta INSERT
        insert_columns = ', '.join(['"' + col + '"' for col in header_row])  # Usar nombres de columna del CSV
        placeholders = ', '.join(['%s'] * n_columns)

        insert_query = f"""
            INSERT INTO "{table_name}" ({insert_columns}) VALUES ({placeholders})
            ON CONFLICT DO NOTHING  """

        print("Query de inserción:", insert_query)

        # Verificar si ya se notifico
        valores_nulos = False
        # Leer los datos del archivo CSV y ejecutar la consulta INSERT
        for row in reader:
            # Verificar si algun valor es nulo o vacio
            if any(cell is None or cell.strip() == '' for cell in row):
                if not valores_nulos:
                    print("Se encontraron valores nulos y/o vacios en la fila. No seran insertados.")
                    valores_nulos = True
                continue
            cursor.execute(insert_query, row)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
