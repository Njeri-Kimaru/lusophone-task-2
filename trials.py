import csv
import requests

with open("Task 2 - Intern.csv", "r", encoding="utf-8-sig") as file:
    content = csv.DictReader(file)
    
    for row in content:
        url = row["urls"]
        
        try:
            status = requests.get(url, timeout=10)
            status_code = status.status_code
        except requests.exceptions.ConnectionError:
            status_code = "CONNECTION ERROR"
        except requests.exceptions.Timeout:
            status_code = "TIMEOUT"
        except requests.exceptions.RequestException:
            status_code = "ERROR"
            
        print(f"({status_code}) {url}")