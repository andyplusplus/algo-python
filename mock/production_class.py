from unittest.mock import MagicMock
from unittest.mock import Mock


class ProductionClass:
    def method(self):
        self.something(1,2,3)
    def something(self, a,b,c):
        pass

    def closer(self, something):
        something.close()

real = ProductionClass()

real.something = MagicMock()
#real.something.assert_called_once_with(1, 2, 3)

mock = Mock()
real.closer(mock)
mock.close.assert_called_with()