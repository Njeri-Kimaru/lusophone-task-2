# Importing libraries
import csv
import requests

def get_status(url):
    url = url.strip()  # removes whitespace 
    # Url's error handling
    try:
        status = requests.get(url, timeout=10)
        status_code = status.status_code
        
        if status_code == 403:
            status_code = "Forbidden"
        elif status_code == 429:
            status_code = "Too Many Requests"

    except requests.exceptions.ConnectionError:
        status_code = "Connection Error"
    except requests.exceptions.Timeout:
        status_code = "Timeout Error"
    except requests.exceptions.RequestException:
        status_code = "General Error"
    return status_code

# Reading into the csv file
if __name__ == "__main__":
    with open("Task 2 - Intern.csv","r", encoding="utf-8-sig") as file: #encoding-removes hidden characters
        content = csv.DictReader(file)
        for c in content:
            # Getting the url from the csv
            url = c['urls'].strip()  # Strip removes space 

            # calling the function to get the status code of the url
            status_code = get_status(url)
            print(f"({status_code}) {url}")