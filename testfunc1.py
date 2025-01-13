import func1
import unittest

class TestFuncs(unittest.TestCase):

    
    def test(self):
        
        # Exercice 1.1 :
        
        # Test liste vide et liste non vide
        
        # self.assertEqual(func1.max_list_int([]), 0)
        # self.assertEqual(func1.max_list_int([1, 2, 3, 4]), -9)
        
        # verif max 
        
        # self.assertEqual(func1.max_list_int([1,2,3,4]),4)
        # self.assertEqual(func1.max_list_int([1,2,3,-4]),3)
        # self.assertEqual(func1.max_list_int([1,9,0,4]),9)
        
        # verif list max values 
        
        # self.assertEqual(func1.max_list_int([1,2,3,4]),[4,3,2])
        # self.assertEqual(func1.max_list_int([1,2,3,-4]),[3,2,1])
        # self.assertEqual(func1.max_list_int([1,9,0,-6]),[9,1,0])
        
        
        #Exercice 1.2 
        # self.assertEqual(func1.est_premier(0),False)
        # self.assertEqual(func1.est_premier(-1),False)
        # self.assertEqual(func1.est_premier(1),False)
        # self.assertEqual(func1.est_premier(4),False)
        # self.assertEqual(func1.est_premier(12),False)
        # self.assertEqual(func1.est_premier(3),True)
        # self.assertEqual(func1.est_premier(5),True)
        
        #Exercice 1.3
        self.assertEqual(func1.est_liste_arithmetique([]),False)
       

if __name__ == '__main__':
    unittest.main()
