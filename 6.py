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
            #Line(points=(100,100,200,200,300,350), #width=10, joint='square')

            self.line = Line(points=(),width=10)

    def on_touch_down(self, touch):
        self.line.points+=(touch.x, touch.y)

class GameApp(App):

    def build(self):
        return PainterWidget()

GameApp().run()
