import unittest
from unittest.mock import patch
from no_return_value import HelloTest


class TestFoo(unittest.TestCase):

    @patch('no_return_value.HelloTest.bar')
    def test_foo_case(self, mock_bar):
        ht = HelloTest()

        ht.foo("some string")
        self.assertTrue(mock_bar.called)
        self.assertEqual(mock_bar.call_args[0][0], "SOME STRING")
