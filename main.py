import interaction as i
import tkinter as tk
from random import randint


class Ball:
    def __init__(self, canvas, window, t_end, x0, vx0, y0, vy0, m_c, x_c, y_c,
                 radius, radius_c):
        self.canvas = canvas
        self.window = window
        self.ball = self.canvas.create_oval(
            x0 * 250 / i.Interaction.ae - radius,
            y0 * 150 / i.Interaction.ae - radius,
            x0 * 250 / i.Interaction.ae + radius,
            y0 * 150 / i.Interaction.ae + radius,
            fill='blue')

        self.ball_c = self.canvas.create_oval(
            x_c * 250 / i.Interaction.ae - radius_c,
            y_c * 150 / i.Interaction.ae - radius_c,
            x_c * 250 / i.Interaction.ae + radius_c,
            y_c * 150 / i.Interaction.ae + radius_c,
            fill='yellow')

        self.interect = i.Interaction(t_end, x0, vx0, y0, vy0, m_c, x_c, y_c)

    def interaction(self):

        self.x = self.interect.solve_func()[0]*250
        self.y = self.interect.solve_func()[1]*150

        return self.x, self.y

    def move_ball(self, counter=0):
        
        if counter < len(self.interaction()[0])-1:
            self.canvas.move(
                self.ball,
                self.interaction()[0][counter + 1] -
                self.interaction()[0][counter],
                self.interaction()[1][counter + 1] -
                self.interaction()[1][counter])
            self.window.after(1, lambda: self.move_ball(counter + 1))
            
#            radius = 2
#            self.canvas.create_oval(
#                self.interaction()[0][counter + 1] -
#                self.interaction()[0][counter]  - radius,
#                self.interaction()[1][counter + 1] -
#                self.interaction()[1][counter]  - radius,
#                self.interaction()[0][counter + 1] -
#                self.interaction()[0][counter] + radius,
#                self.interaction()[1][counter + 1] -
#                self.interaction()[1][counter] +  - radius,
#                fill='yellow')
            
        else:
            self.canvas.move(self.ball, 1500, 900)

window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=600, bg='black')
canvas.pack()


def create_func():
    x0 = randint(1, 3)*149 * 10**9
    y0 = randint(1, 3)*149 * 10**9
    vy0 = randint(5000, 30000)
    
    ball = Ball(canvas,
                window,
                t_end=24 * 3600 * 365,
                x0=x0,
                vx0=0,
                y0=y0,
                vy0=vy0,
                m_c=1.9885 * 10**30,
                x_c=2 * 149 * 10**9,
                y_c=2 * 149 * 10**9,
                radius=5,
                radius_c=20)

    ball.move_ball()


tk.Button(window, text='Create ball', command=create_func).pack()

window.mainloop()
