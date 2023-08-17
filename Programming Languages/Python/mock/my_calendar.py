# looks up an object in a given module and replace it with a Mock


import requests
from datetime import datetime


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

# as a Decorator :
# mock for the entire duration of the entire test function
