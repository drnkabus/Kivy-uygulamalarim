from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class MainLayout(BoxLayout):
    sonuc = StringProperty("Butona Bas")

    def degistir(self):
        self.sonuc = "Merhaba Kivy!"

class MyApp(App):
    def build(self):
        return MainLayout()

MyApp().run()