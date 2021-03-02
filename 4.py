from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class GameApp(App):

    def ivent_press(self, instance):
        if self.lbl.text == 'Nice':
            self.lbl.text = 'Bad'
        else:
            self.lbl.text = 'Nice'

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50)

        self.btn_1 = Button(text='Press me', on_press = self.ivent_press)
        self.lbl = Label(text='Change me')
        self.layout.add_widget(self.btn_1)
        self.layout.add_widget(self.lbl)

        return self.layout

GameApp().run()
