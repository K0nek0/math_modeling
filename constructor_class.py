class Ball:
    
    #создание конструктора  
    def __init__(self, color, radius):
        print('Я родился')
        
        self.color = color
        self.radius = radius
        
    def update_parameters(self, new_color, new_radius):
        self.color = new_color
        self.radius = new_radius
        
    def printer(self):
        print(f'Текущий цвет: {self.color}')
        print(f'Текущий радиус: {self.radius}')
        
ball = Ball('red', 8)
ball_krutoi = Ball('o4enred', 800)

#
ball.printer()

print(ball.color)
ball.update_parameters('white', 9)
print(ball.color)

ball.printer()
#
