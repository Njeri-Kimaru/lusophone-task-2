import requests
from status_code import get_status
import unittest
from unittest.mock import patch, MagicMock

class TestFetchURLStatus(unittest.TestCase):

    @patch('status_code.requests.get')  # Patch the requests.get inside my module
    def test_get_status_success(self, mock_get):
        """Test get_status function with a 200 OK response."""
        mock_response = MagicMock()
        mock_response.status_code = 200  # Simulate a successful response
        mock_get.return_value = mock_response  # Mock the return value of requests.get
        
        result = get_status("https://example.com")
        self.assertEqual(result, 200)  

    @patch('status_code.requests.get')  # Patch requests.get
    def test_get_status_not_found(self, mock_get):
        """Test get_status function with a 404 Not Found response."""
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a 404 response
        mock_get.return_value = mock_response  # Mock the return value of requests.get
        
        result = get_status("https://google.com")
        self.assertEqual(result, 404)  

    @patch('status_code.requests.get')  # Patch the requests.get inside my module
    def test_get_status_forbidden(self, mock_get):
        """Test get_status function with a 403 Forbidden response."""
        mock_response = MagicMock()
        mock_response.status_code = 403  # Simulate a forbidden response
        mock_get.return_value = mock_response  # Mock the return value of requests.get
        
        result = get_status("https://example.com")
        self.assertEqual(result, "Forbidden")  

    @patch('status_code.requests.get')  # Patch the requests.get inside my module
    def test_get_status_too_many_requests(self, mock_get):
        """Test get_status function with a 429 Too Many Requests response."""
        mock_response = MagicMock()
        mock_response.status_code = 429  # Simulate a 'too many requests' response
        mock_get.return_value = mock_response  # Mock the return value of requests.get
        
        result = get_status("https://example.com")
        self.assertEqual(result, "Too Many Requests")   


    @patch('status_code.requests.get')  # Patch requests.get
    def test_get_status_connection_error(self, mock_get):
        """Test get_status function when there's a connection error."""
        mock_get.side_effect = requests.exceptions.ConnectionError  # Simulate connection error
        
        result = get_status("invalid-url")
        self.assertEqual(result, "Connection Error")  

    @patch('status_code.requests.get')  # Patch the requests.get
    def test_get_status_timeout(self, mock_get):
        """Test get_status function when there's a timeout."""
        mock_get.side_effect = requests.exceptions.Timeout  # Simulate timeout error
        
        result = get_status("https://example.com")
        self.assertEqual(result, "Timeout Error")

    @patch('status_code.requests.get')  # Patch the requests.get
    def test_get_status_general_error(self, mock_get):
        """Test get_status function when there's a general request error."""
        mock_get.side_effect = requests.exceptions.RequestException  # Simulate a general request error
        
        result = get_status("https://example.com")
        self.assertEqual(result, "General Error")  

if __name__ == "__main__":
    unittest.main()