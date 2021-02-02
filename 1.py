class Human:

    default_name = 'Niko'
    default_edge = 21
    
    def __init__(self, name=default_name, edge=default_edge):
        self.name = name
        self.edge = edge
        
        self._money = 50
        self._house = '2'
        
             
    def info(self):
        print(f'Ваше имя: {self.name}, возраст: {self.edge}, \nКол-во денег: {self._money}, тип дома: {self._house}' )
    
    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_edge)
    
        
    def _make_deal(self, price, house):
        self.price = 500
        self._money -= self.price
        self.house = house
        
        return self._money
    
    def earn_money(self):
        self.money_for_job = 1000
        self._money += self.money_for_job
        
    def buy_house(self, house):
        self.house = house
        if self._money < self.house.final_price(5):
            print('У вас слишком мало денег')
            print(f'Не хватает {self._money - self.house.price}')
        else:
            print('Вы успешно приобрели дом')

class House:
    
    def __init__(self, area, price):
        self._area = area
        self._price = price
        
    def final_price(self, discount):
        self.discount = discount
        self._price = self._price - (self._price/discount * 100)
        
        return self._price
        
class SmallHouse(House):
    
    default_area = 40
    
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

Human.default_info()

human = Human('vasya', 30)
human.info()
    
smallhouse = SmallHouse(1000)
    
human.earn_money()
human.buy_house(smallhouse)
    
    
    
    
    
    