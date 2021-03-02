from kivy.app import App
from kivy.uix.button import Button

class GameApp(App):
    
    def build(self):
        return Button(text='Hello World')
    
GameApp().run()
