from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class PainterWidget(Widget):

    def __init__(self):
        super(PainterWidget, self).__init__()

        with self.canvas:
            Color(0,1,1,1)
            Ellipse(pos=(100,100), size=(50,50))

class GameApp(App):

    def build(self):
        return PainterWidget()

GameApp().run()
