import numpy as np

class Tomato:
    
    states = {0:'Отсутствует', 1:'Цветение', 2:'Зеленый', 3:'Красный'}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
        
    def grow(self):
        self.state += 1
        print('Томат сейчас {}')
    
    def is_ripe(self):
        
        if self.state == 3:
            print('Томат успешно созрел')
            
class TomatoBush:
    
    def __init__(self, tomatoes):
        self.tomatoes = []
        for i in range(0, tomatoes, 1):      
            self.tomatoes.append(Tomato(i))
            
    
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
            
    def all_are_ripe(self):
        if self.tomatoes == 3:
            True
    
    def give_away_all(self):
        self.tomatoes = []
        
class Gardener:
    
            
            
            
            
            