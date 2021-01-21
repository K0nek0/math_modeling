class Ball:
    def __init__(self):
        #public
        self.name = 'Oval'
        
        #private
        self._radius = 50
        
        #protected
        self.__color = 'red'
        
    #public method
    def name_func(self):
        print(self.name)
        
    def new_color(self):
        print(self.__update_color() + ' True')
        
    #private method
    def _update_radius(self):
        self._radius += 1
        
    #protected method
    def __update_color(self):
        return self.__color

ball = Ball()
print(ball.name)
print(ball._radius) #можно, но не хорошо
print(ball._Ball__color) #можно, но не хорошо

ball.new_color()
