import requests
import time
import json

url = "https://api.quotable.io/random"

quotes = requests.get(url)
print(quotes.json())

try:  # hacer la solicitud a la API
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (codigo de estado 200)
    if response.status_code == 200:
        # Intentar analizar el JSON
        quotes = response.json()
        print(quotes)
    else:
        print(
            f" Error en la solicitud. Codigo de estado: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f'Error en la solicitud: {e}')
except json.decoder.JSONDecodeError as e:
    print(f'Error al decodificar JSON: {e}')


def quote_getter():
    x = 0
    cool_list = []
    while x < 10:
        time.sleep(5)
        cool_list.append(quotes)
        x += 1
    return cool_list


def json_quote_list(x):
    with open("inspirational_quotes.json", "w", encoding="utf-8") as file:
        jsonString = json.dumps(x, indent=3)
        file.write(jsonString)


json_quote_list(quote_getter())
