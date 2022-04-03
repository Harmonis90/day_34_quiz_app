import requests


parameters = {
    'amount': 10,
    'type': 'boolean'
}
connection = requests.get("https://opentdb.com/api.php", params=parameters)
connection.raise_for_status()
question_data = connection.json()["results"]
