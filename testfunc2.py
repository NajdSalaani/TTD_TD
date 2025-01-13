import unittest
from func2 import FIFO 
from func2 import LIFO

class Test(unittest.TestCase):
    
    def test(self):
        #Pour FIFO
        # fifo = FIFO()
        # self.assertEqual(fifo.est_vide(),True)
        
        # fifo.ajout(10)
        # self.assertEqual(fifo.est_vide(),False)
        # fifo.ajout(15)
        # self.assertEqual(fifo.queue,[10,15])
        # self.assertEqual(fifo.size(), 2)
        
        # fifo.retire()
        # self.assertEqual(fifo.queue,[15])
        # fifo.retire()
        # self.assertEqual(fifo.est_vide(),True)
        
        #Pour LIFO
        
        lifo = LIFO()
        self.assertEqual(lifo.est_vide(),True)
        self.assertEqual(lifo.size(), 0)
        

if __name__ == '__main__':
    unittest.main()
