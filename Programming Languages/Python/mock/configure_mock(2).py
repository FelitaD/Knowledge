from unittest.mock import Mock

# response_mock = Mock()

# response_mock.json.return_value = {
#     '12/25': 'Noel',
#     '03/05': 'Anniversaire'
# }

holidays = {'12/25': 'Noel', '03/05': 'Anniversaire'}

response_mock = Mock(**{'json.return_value': holidays})
