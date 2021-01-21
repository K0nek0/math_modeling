import numpy as np

class Ball:
    
    def __init__(self, color, end_time):
        self.color = color
        self.time = np.arange(0, end_time, 0.1)
        
    def move_ball(self, vx, vy):
        self.x = vx*self.time
        self.y = vy*self.time
        print(self.x)
        print(self.y)
        
#super class
class Football(Ball):
    def __init__(self, aerodynamics, color):
        super().__init__(color=color, end_time=10)
        self.aerodynamics = aerodynamics
        
    def fly(self):
        if self.aerodynamics == 'circle':
            print('True fly')
        else:
            print('Bad ball')
            
ball = Football('oval', 'green')
ball.fly()
ball.move_ball(6, 7)
    