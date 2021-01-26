class Human:

    default_name = 'Niko'
    default_edge = 21
    
    def __init__(self, name, edge):
        self.name = Human.default_name
        self.edge = Human.default_edge
        
        self._money = 50
        self._house = '2'
        
             
    def info(self):
        print(f'Ваше имя: {self.name}, возраст: {self.edge}, \nКол-во денег: {self._money}, тип дома: {self._house}' )
    
    @staticmethod
    def default_info():

        pass
    
        
    def _make_deal(self, price):
        self.price = 500
        self._money -= self.price
        self._house = self.house
    
    def earn_money(self, money_for_job):
        self.money_for_job = 1000
        self._money += self.money_for_job
        
    def buy_house(self):
        if self._money < self.price:
            print('У вас слишком мало денег')
        else:
            pass

human = Human('', 3)
human.info()