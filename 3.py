from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class GameApp(App):

    def ivent_press(self, instance):
        print(instance.text)
        self.btn_1.text = 'Nice'


    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50)

        self.btn_1 = Button(text='Press me', on_press = self.ivent_press)
        self.layout.add_widget(self.btn_1)

        return self.layout


GameApp().run()
