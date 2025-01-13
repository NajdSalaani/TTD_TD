import unittest
from func2 import FIFO 

class Test(unittest.TestCase):
    
    def test(self):
        fifo = FIFO()
        self.assertTrue(fifo.queue == [])


if __name__ == '__main__':
    unittest.main()
