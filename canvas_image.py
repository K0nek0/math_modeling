import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

img = Image.open('1.gif')
pic = ImageTk.PhotoImage(img)

canvas = tk.Canvas(width=img.size[0]+20,
                   height=img.size[1]+20)

canvas.create_image(400,400,
                    image=pic)

canvas.pack()

window.mainloop()
