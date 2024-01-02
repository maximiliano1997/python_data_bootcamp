import json

# mis credenciales
hostname = "localhost"
database = "playground"
username = "postgres"
password = "root"
port_id = 5432


# Function to ceate a table in PostgreSQL with user input

def create_table():
    # Solicitar al usuario el nombre de la tabla
    name_table = input("Plase name your table: ")

    # Solicitar al usuario el numero de columnas en la tabla
    number_columns = input("How many columns do you need?")

    # Inicializar listas vacias para almacenar nombres de columnas, tipos de datos y sus combinaciones
    list_columns = []
    list_records = []
    number_index = 0

    # Bucle para recopilar nombres de columnas y tipos de datos para cada columna
    while number_index < int(number_columns):
        # Solicitar al usuario el nombre de la columna
        list_columns.append(
            input(f"Column Number {number_index} name please:  "))

        # Solicitar al usuario el tipo de datos de la columna
        list_records.append(input(
            f"Please enter datatype (please be very specific - e.g. if you use varchar() plase also put a number into the bracekts:  )"))

        # Incrementar el indice de la columna
        number_index += 1

    # Combinar nombre de columnas y tipos de datos en una lista de cadenas
    lists_records = []
    for column_name, column_type in zip(list_columns, list_records):
        string_placeholder = f"{column_name} {column_type}"
        lists_records.append(string_placeholder)

    records_printed = (" ,".join(lists_records))
    create_script = f'''CREATE TABLE IF NOT EXISTS {name_table} ({records_printed})'''

    return create_script
