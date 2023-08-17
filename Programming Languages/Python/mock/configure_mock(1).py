from unittest.mock import Mock

# mock = Mock()

# mock.side_effect = KeyError
# mock.call_count = 0
# mock.return_value = True

mock = Mock(return_value=True, side_effect=KeyError)

# mock()

mock.configure_mock(side_effect=None)

print(mock.return_value)
print(mock.side_effect)

mock()

