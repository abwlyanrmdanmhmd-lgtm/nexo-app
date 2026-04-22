from kivy.app import App
from kivy.uix.label import Label

class NexoApp(App):
    def build(self):
        return Label(text='Ammar Ya Misr\nWelcome Ramadan!')

if __name__ == '__main__':
    NexoApp().run()