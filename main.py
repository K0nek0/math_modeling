import interaction as i
import tkinter as tk
from random import randint


class Ball:
    def __init__(self, canvas, window, t_end, x0, vx0, y0, vy0, radius):
        self.canvas = canvas
        self.window = window
        self.ball = self.canvas.create_oval(
            x0 * 250 / i.Interaction.ae - radius,
            y0 * 150 / i.Interaction.ae - radius,
            x0 * 250 / i.Interaction.ae + radius,
            y0 * 150 / i.Interaction.ae + radius,
            fill='blue')

        self.interect = i.Interaction(t_end, x0, vx0, y0, vy0)

    def interaction(self):

        self.x = self.interect.solve_func()[0] * 250
        self.y = self.interect.solve_func()[1] * 150

        return self.x, self.y

    def move_ball(self, counter=0):

        if counter < len(self.interaction()[0]) - 1:
            self.canvas.move(
                self.ball,
                self.interaction()[0][counter + 1] -
                self.interaction()[0][counter],
                self.interaction()[1][counter + 1] -
                self.interaction()[1][counter])
            self.window.after(1, lambda: self.move_ball(counter + 1))
        else:
            self.canvas.move(self.ball, 1500, 900)


window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=600, bg='black')

radius_c = 20
ball_c = canvas.create_oval(
    i.Interaction.x_c * 250 / i.Interaction.ae - radius_c,
    i.Interaction.y_c * 150 / i.Interaction.ae - radius_c,
    i.Interaction.x_c * 250 / i.Interaction.ae + radius_c,
    i.Interaction.y_c * 150 / i.Interaction.ae + radius_c,
    fill='yellow')
canvas.pack()


def create_func():
    x0 = randint(1, 3) * 149 * 10**9
    y0 = randint(1, 3) * 149 * 10**9
    vy0 = randint(10000, 30000)

    ball = Ball(canvas,
                window,
                t_end=24 * 3600 * 365,
                x0=x0,
                vx0=0,
                y0=y0,
                vy0=vy0,
                radius=5)

    ball.move_ball()


tk.Button(window, text='Create ball', command=create_func).pack()

window.mainloop()
