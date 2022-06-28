from kivymd.app import MDApp
from kivy.lang import Builder

class App(MDApp):
    def build(self):
        return Builder.load_file("./views/home.kv")
    
App().run()