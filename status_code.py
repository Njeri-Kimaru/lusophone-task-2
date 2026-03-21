# Importing libraries
import csv
import requests

# Reading into the csv file
with open("Task 2 - Intern.csv","r", encoding="utf-8-sig") as file: #encoding-removes hidden characters
    content = csv.DictReader(file)
    for c in content:
        # Getting the url from the csv
        url = c["urls"]

    # Url's status
        try:
            status = requests.get(url, timeout=20)
            status_code = status.status_code
        except requests.exceptions.ConnectionError:
            status_code = "Connection error"
        except requests.exceptions.Timeout:
            status_code = "Timeout"
        except requests.exceptions.RequestException:
            status_code = "Error"

        print(f"({status_code}) {url})")


