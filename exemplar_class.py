class Ball:
    
    x_coord = 0
    y_coord = 0
    
    def move_func(self, vx, vy, t):
        self.x = vx * t + Ball.x_coord
        self.y = vy * t + Ball.y_coord
        
        print(f'Переместились в ({self.x}, {self.y})')
        
        Ball.x_coord += 1
        Ball.y_coord += 1
        
ball = Ball() #экземпляр класса

ball.move_func(6, 5, 7)

print(ball.x_coord)
print(Ball.x_coord)

ball_1 = Ball()
print(ball_1.x_coord)

print(ball.x)

ball_1.move_func(3, 5, 7)
print(ball_1.x)
