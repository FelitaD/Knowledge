from unittest.mock import create_autospec

import my_calendar

calendar = create_autospec(my_calendar)

print(calendar)

calendar.is_weekday()
calendar.is_weekdayy()
