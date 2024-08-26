from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import serial

def callback(instance):
    ser = serial.Serial('COM1', 9600, timeout=0)
    data = ser.read()
    msg = ""
    if str(data)[3:]=="":
        msg = "Новых сообщений нет."
    else:
        msg = "Последнее сообщение: "+str(data)[3:]

class LoginScreen(FloatLayout):
    def __init__(self, **kwargs):
        ser = serial.Serial('COM1', 9600, timeout=0)
        ser.read()
        super(LoginScreen, self).__init__(**kwargs)
        data = ser.read()
        msg = ""
        if str(data)[3:]=="":
           msg = "Новых сообщений нет."
        else:
           msg = "Последнее сообщение: "+str(data)[3:]
        self.add_widget(Label(text=msg, pos_hint={'x':0, 'y':0.2}, font_size=30))
        btn0 = Button(text="Обновить", size_hint=(.4,.15), pos_hint={'x':0.4, 'y':0.3}, font_size=30)
        btn0.bind(on_press=callback)
        self.add_widget(btn0)
        self.add_widget(Label(text="Отправить сообщение:", pos_hint={'x':0, 'y':0}, font_size=20))
        self.add_widget(TextInput(text='Hello world', pos_hint={'x':0.2, 'y':.1}, size_hint=(.5,.15)))
class MyApp(App):

  def build(self):
    return LoginScreen()
if __name__ == '__main__':
  MyApp().run()