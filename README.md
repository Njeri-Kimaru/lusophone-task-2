# Creating a Python script to get and print the status code of the response of a list of URLs from a .csv file.

This repository contains my submission for the second task on the wikimedia project addressing the lusophone techonlogical wishlist proposals.

### | File | Description |
| `status_code.py` | Main script — reads the CSV and prints each URL's status code 
| `test_status_code.py`|  Unit tests covering expected behaviour and error handling.
| `Task 2 - Intern.csv`| The CSV file containing the list of URLs.
| `requirements.txt`| Contains the libraries I used.
| `.gitignore`| Contains my virtual environment.

---

### What the Code Does

`status_code.py`:

1. Opens `Task 2 - Intern.csv` and iterates over every row.
2. Skips empty rows and any row whose value does not begin with `http` (e.g. header rows).
3. Sends an HTTP GET request to each URL with a 10-second timeout.
4. Prints the result in the required format:

   ```
   (STATUS CODE) URL
   ```

#### Example
   ```
   (200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-...
   (404) https://www.example.com/missing-page
   (ERROR) https://www.broken-site.com — Connection refused
   ```

5. If a network error occurs (timeout, DNS failure, etc.) it prints `(ERROR)` followed by the URL and the error message, instead of crashing.

---

###  Tests — test_status_code.py

The test suite uses Python's built-in `unittest` framework together with `unittest.mock` so that no real HTTP requests are made during testing.
```
test_get_status_success (test_status_code.TestFetchURLStatus.test_get_status_success)
Test get_status function with a 200 OK response. ... ok      
test_get_status_timeout (test_status_code.TestFetchURLStatus.test_get_status_timeout)
----------------------------------------------------------------------
Ran 7 tests in 0.XXXs

OK
### Running the tests

```bash
python -m unittest test_status_code.py -v
```

Expected output:

```

test_get_status_connection_error ................. ok
test_get_status_forbidden ........................ ok
test_get_status_general_error .................... ok
test_get_status_not_found ........................ ok
test_get_status_success .......................... ok
test_get_status_timeout .......................... ok
test_get_status_too_many_requests ................ ok

----------------------------------------------------------------------
Ran 7 tests in 0.XXXs

OK
```
### Tools used
- python
- bash
