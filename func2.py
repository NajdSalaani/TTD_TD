
#Exercice 2 : FIFO

class FIFO:
    def __init__(self):
        self.queue = [] 

    def ajout(self, value):
        self.queue.append(value)
       

    def retire(self):
        print("pass")
    
    def est_vide(self):
        if self.queue == [] :
            return True 
        return False

    def size(self):
        print("pass")
        
