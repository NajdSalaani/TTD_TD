import unittest
from func2 import FIFO 

class Test(unittest.TestCase):
    
    def test(self):
        fifo = FIFO()
        self.assertEqual(fifo.est_vide(),True)


if __name__ == '__main__':
    unittest.main()
