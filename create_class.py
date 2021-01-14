class Ball:
    
    #атрибуты класса
    color = 'red'
    radius = 5
    
    def update_parameter(self):
        print('Цвет поманяли')
        
    def move_ball(self, vx0=0):
        print(f'Мячик преобрел скорость {vx0}')
        
#экзепляр класса
ball_1 = Ball()
ball_2 = Ball()

print(type(ball_1))
print(type(2))

ball_1.move_ball()
print(ball_2.color)