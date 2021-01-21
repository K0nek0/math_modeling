import numpy as np

class Ball:
    
    x_coords = 0
    y_coords = 0
    
    def __init__(self, end_time):
        self.time = np.arange(0, end_time, 0.1)
        
    #методы экземпляра класса
    def move_ball(self, vx, vy):
        self.x = vx*self.time + Ball.x_coords
        self.y = vy*self.time + Ball.y_coords
        
        print(f'Coords ball \n x:{self.x} \n y:{self.y}')
        
    #статический метод
    @staticmethod
    def ball_helper(image_ball):
        if image_ball == 'hexagone':
            color = 'red'
            print(color)
        else:
            print('blue')
            
    #методы класса
    @classmethod
    def toy_ball(cls, end_time):
        toy_ball = cls(10)
        
        return toy_ball
    
#ball = Ball(15)
#ball.move_ball(3, 5)

Ball(15).move_ball(3, 5)
Ball.ball_helper('hexagone')
#ball.ball_helper('hexagon')
        
toy_1 = Ball.toy_ball(10)
print(toy_1)
        