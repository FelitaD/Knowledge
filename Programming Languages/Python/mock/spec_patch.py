from unittest.mock import patch

import my_calendar

with patch('__main__.my_calendar', autospec=True) as calendar:
    calendar.is_weekday()
    calendar.is_weekdayy()
