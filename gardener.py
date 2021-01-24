class Tomato:
    
    states = {0:'Отсутствует', 1:'цветет', 2:'зеленый', 3:'красный'}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
        
    def grow(self):
        self._IncreaseState()
        print(f"Помидор {self.index}: {self.states[self.state]}")
            
    def _IncreaseState(self):
        self.state += 1
        if self.state >= 3:
            self.state = 3
    
    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False
            
class TomatoBush:
    
    def __init__(self, tomatoes):
        self.tomatoes = []
        for i in range(1, tomatoes + 1):      
            self.tomatoes.append(Tomato(i))
            
    
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
            
    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe() == False:
                return False
        return True
    
    def give_away_all(self):
        self.tomatoes = []
        
class Gardener:
    
    def __init__(self, bush):
        self.bush = bush
        
    def work(self):
        self.bush.grow_all()
        
    def harvest(self):
        if self.bush.all_are_ripe() == True:
            self.bush.give_away_all()
            print("Помидорки созрели и были собраны")
            return True
        else:
            print("Помидорки еще не созрели")
            return False

bush = TomatoBush(3)
gard = Gardener(bush)

while True:
    if gard.harvest() == True:
        break
    else:
        gard.work()
        