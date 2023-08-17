from unittest.mock import Mock
from pprint import pprint

calendar = Mock(spec=['is_weekday', 'get_holidays'])

pprint(dir(calendar))

calendar.is_weekday()
calendar.is_weekdayy()