from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import serial

def callback1(instance):
   pass

def callback0(instance):
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
        btn0 = Button(text="Обновить", size_hint=(.4,.15), pos_hint={'x':0.25, 'y':0.5}, font_size=30)
        self.add_widget(TextInput(text='Позывной:', pos_hint={'x':0.35, 'y':.1}, size_hint=(.3,.15)))
        btn0.bind(on_press=callback0)
        self.add_widget(btn0)
        btn1 = Button(text="Отправить", size_hint=(.4,.15), pos_hint={'x':0.25, 'y':.1},  font_size=30)
        btn1.bind(on_press=callback1)
        self.add_widget(btn1)
        self.add_widget(TextInput(text='Сообщение:', pos_hint={'x':0.3, 'y':0.3}, size_hint=(.3,.15)))
class MyApp(App):

  def build(self):
    return LoginScreen()
if __name__ == '__main__':
  MyApp().run()