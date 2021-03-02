from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class GameApp(App):
    
    def build(self):
        layouts = BoxLayout(orientation = 'vertical',
                            padding = 50)

        layout_btn = GridLayout(cols = 4)
        layout_txt = BoxLayout()

        label = Label(text = 'My App')
        layout_txt.add_widget(label)

        text = TextInput(text = 'input text')
        layout_txt.add_widget(text)

        for i in range(16):
            btn = Button(text = f'Кнопка {i+1}')
            layout_btn.add_widget(btn)

        layouts.add_widget(layout_txt)
        layouts.add_widget(layout_btn)
        
        return layouts

GameApp().run()
