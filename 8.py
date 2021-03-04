from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Line

class PainterWidget(Widget):
    
    def __init__(self):
        super(PainterWidget, self).__init__()

        with self.canvas:
            Color(0,1,1,1)
            for i in range(0,100):
                x =+ i
                y =+ i
                Ellipse(pos=(x,y), size=(25,25))
                
class GameApp(App):

    def build(self):
        
        return PainterWidget()

GameApp().run()
