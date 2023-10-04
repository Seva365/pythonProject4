from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
Window.size = (360, 640)
Builder.load_string('''<MyOwnButton@MDRaisedButton>:
    md_bg_color: "#FFCA33"
    text_color: "white"
    font_size: 50
<Container>
    orientation: 'vertical'
    button7: button7
    button8: button8
    button9: button9
    buttonmult: buttonmult
    button4: button4
    button5: button5
    button6: button6
    buttonplus: buttonplus
    button1: button1
    button2: button2
    button3: button3
    buttonmin: buttonmin
    buttonAC: buttonAC
    buttonpoint: buttonpoint
    button0: button0
    buttondiv: buttondiv
    label: label
    buttoneq: buttoneq
    AnchorLayout:
        anchor_y: 'top'
        size_hint: 1, 0.1
        MDLabel:
            text: '0'
            font_size: '35sp'
            id: label
    GridLayout:

        size_hint: 1, 0.8
        rows: 5
        columns: 4
        MyOwnButton:
            text: '7'
            size_hint: 0.25, 0.20
            id: button7
            on_press:
                root.think('7')
        MyOwnButton:
            text: '8'
            size_hint: 0.25, 0.20
            id: button8
            on_press:
                root.think('8')
        MyOwnButton:
            text: '9'
            size_hint: 0.25, 0.20
            id: button9
            on_press:
                root.think('9')
        MyOwnButton:
            text: '*'
            size_hint: 0.25, 0.20
            id: buttonmult
            on_press:
                root.think('*')
        MyOwnButton:
            text: '4'
            size_hint: 0.25, 0.20
            id: button4
            on_press:
                root.think('4')
        MyOwnButton:
            text: '5'
            size_hint: 0.25, 0.20
            id: button5
            on_press:
                root.think('5')
        MyOwnButton:
            text: '6'
            size_hint: 0.25, 0.20
            id: button6
            on_press:
                root.think('6')
        MyOwnButton:
            text: '/'
            size_hint: 0.25, 0.20
            id: buttondiv
            on_press:
                root.think('/')
        MyOwnButton:
            text: '1'
            size_hint: 0.25, 0.20
            id: button1
            on_press:
                root.think('1')
        MyOwnButton:
            text: '2'
            size_hint: 0.25, 0.20
            id: button2
            on_press:
                root.think('2')
        MyOwnButton:
            text: '3'
            size_hint: 0.25, 0.20
            id: button3
            on_press:
                root.think('3')
        MyOwnButton:
            text: '-'
            size_hint: 0.25, 0.20
            id: buttonmin
            on_press:
                root.think('-')
        MyOwnButton:
            text: '0'
            size_hint: 0.25, 0.20
            id: button0
            on_press:
                root.think('0')
        MyOwnButton:
            text: '.'
            size_hint: 0.25, 0.20
            id: buttonpoint
            on_press:
                root.think('.')
        MyOwnButton:
            text: 'AC'
            size_hint: 0.25, 0.20
            id: buttonAC
            on_press:
                root.clear()
        MyOwnButton:
            text: '+'
            size_hint: 0.25, 0.20
            id: buttonplus
            on_press:
                root.think('+')


    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 0.15

        MyOwnButton:
            size_hint: 1, 0.1
            text: '='
            id: buttoneq

            font_size:100
            on_press:
                root.calc()
''')
class Container(BoxLayout):
    formula = ''
    def think(self, button):
        if self.formula == '':
            self.label.text = button
            self.formula += button
        elif button == '+' or button == '-' or button == '*' or button == '/':
            self.label.text = ''
            self.formula += button
        else:
            self.label.text += button
            self.formula += button
    def clear(self):
        self.label.text = ''
        self.formula = ''
    def calc(self):
        try:
            self.label.text = str(eval(self.formula))
            self.formula = ''
        except:
            self.label.text = 'ошибка'

class CalcApp(MDApp):
    def __init__(self, **kwargs):
        self.title = 'Калькулятор'

        super().__init__(**kwargs)
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()
if __name__ == '__main__':
    CalcApp().run()