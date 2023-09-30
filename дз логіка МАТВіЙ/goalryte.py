
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScr(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="horizontal")
        vbox = BoxLayout(orientation="vertical")

        txt = Label(text="Виберіть екран")
        btn1 = Button(text="1 екран")
        btn2 = Button(text="2 екран")

        btn1.on_press = self.next
        btn2.on_press = self.next2
        
        vbox.add_widget(btn1)
        vbox.add_widget(btn2)

        hbox.add_widget(txt)
        hbox.add_widget(vbox)

        self.add_widget(hbox)
    def next(self):
        self.manager.current = 'second'
        self.manager.transition.direction = 'left'
    def next2(self):
        self.manager.current = 'three'
        self.manager.transition.direction = 'left'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)

        gbox = BoxLayout(orientation="vertical")

        btn = Button(text="назад.")
        txt = Label(text="хто це на картинці?")
        btn.on_press = self.next

        gbox.add_widget(txt) 
        gbox.add_widget(btn)
       

        self.add_widget(gbox)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class FirstScr(Screen):
    def __init__(self, name='three'):
        super().__init__(name=name)

        gbox = BoxLayout(orientation="vertical")
        btn = Button(text="назад")
        btn.on_press = self.next
        img = Image(source='enot.png')

        gbox.add_widget(img) 
        gbox.add_widget(btn)
       

        self.add_widget(gbox)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(SecondScr())
        sm.add_widget(FirstScr())



        return sm

app = MyApp()
app.run()