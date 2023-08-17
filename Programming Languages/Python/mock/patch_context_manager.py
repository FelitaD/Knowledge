import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()


# Why using context manager :
# need to mock only for a part of test scope
# already using too many decorators or parameters
# when 'with' exits, the mock disappears

