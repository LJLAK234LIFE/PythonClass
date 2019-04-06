from myMath import Geometric
from myMath import Arithmatic

class Mathematic:

    def __init__(self, a = Arithmatic(), pqr = Geometric()):
        self._arithmatic = a
        self._geometrics = pqr

    @property
    def arithmatic(self):
        return self._arithmatic

    @property
    def geometric(self):
        return self._geometrics

    def Add(self, x, y):
        result = self.arithmatic.Add(x, y)
        print('Sum of two numbers: ' + str(result))

    def Multiply(self, x, y):
        result = self.geometric.Multiplication(x, y)
        print('Multiplication of two numbers: ' + str(result))


