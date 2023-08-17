# ≠ Monkey patching = replacement in the same file

import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests') # patch requests here rather than in the local scope
    def test_get_holidays_timeout(self, mock_requests): # new parameter to pass the mock object
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()


# patch is an instance of Magick Mock
# MagicMock implements magic methods such as .__len__ __str__ __iter__

