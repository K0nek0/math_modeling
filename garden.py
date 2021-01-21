class Tomato:
    
    states = {0:'Отсутствует', 1:'цветет', 2:'зеленый', 3:'красный'}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
        
    def grow(self):
        self.state += 1
        print(f'Томат сейчас {self.states[self.state]}')
    
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
            return True
    
    def give_away_all(self):
        self.tomatoes = []
        
class Gardener:
    
    def __init__(self, name, plant):
        self.name = name
        self.plant = TomatoBush()
        
#    def work(self)
#    def harvest(self)
#    def knowledge_base(self):
        
bush = TomatoBush(5)
bush.grow_all()
bush.grow_all()
        