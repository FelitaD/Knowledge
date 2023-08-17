import requests
import unittest
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()
# a quoi ca sert d'importer requests? ->
# on peut mocker que des methodes qui existent vraiment mais on peut passer n'importe quel argument


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        # get() forwards its arguments to log_request()
        # 'http://localhost/api/holidays' passed as url in log_requests
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == '__main__':
    unittest.main()
