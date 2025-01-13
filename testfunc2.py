import unittest
from func2 import FIFO 

class Test(unittest.TestCase):
    
    def test(self):
        
        fifo = FIFO()
        self.assertEqual(fifo.est_vide(),True)
        
        fifo.ajout(10)
        self.assertEqual(fifo.est_vide(),False)


if __name__ == '__main__':
    unittest.main()
