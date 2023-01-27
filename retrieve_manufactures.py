"""
Write a script to connect to the following API ["https://swapi.dev/api/vehicles/"].
Retrieve the JSON data, and list the first 5 unique manufacturers.
"""

import requests
import json


def retrieve_five_unique_manufactures():
    response = requests.get("https://swapi.dev/api/vehicles/")
    data = json.loads(response.text).get("results")

    count = 0
    manufacturers = set()

    while count <= 5:
        manufacturers.add(data[count].get("manufacturer"))
        count += 1

    return manufacturers
