import unittest
from unittest.mock import patch, MagicMock, Mock

import module
from module import ProductionClass


class TestModule(unittest.TestCase):

    @patch('module.ClassName2')
    @patch('module.ClassName1')
    def test_mock_class_patch(self, MockClass1, MockClass2):
        module.ClassName1()
        module.ClassName2()
        assert MockClass1 is module.ClassName1
        assert MockClass2 is module.ClassName2
        assert MockClass1.called
        assert MockClass2.called

    def test_patch_context(self):
        with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
            thing = ProductionClass()
            thing.method(1, 2, 3)

    def test_patch_dict(self):
        foo = {'key': 'value'}
        original = foo.copy()
        with patch.dict(foo, {'new_key': 'new_value'}, clear=True):
            assert foo == {'newkey': 'newvalue'}
        assert foo == original

    def test_magic_method(self):
        mock = MagicMock()
        mock.__str__.return_value = 'foobarbaz'
        print(str(mock))
        mock.__str__.assert_called_with()


if __name__ == '__main__':
    unittest.main()
