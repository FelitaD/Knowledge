from unittest.mock import Mock
import my_calendar


calendar = Mock(spec=my_calendar)

print(dir(calendar))

calendar.is_weekday()
calendar.is_weekdayy()