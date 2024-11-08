import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout  # Use FloatLayout to match .kv file layout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

kivy.require('1.9.0')


class MyRoot(FloatLayout):  # Change to FloatLayout to match .kv file structure
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

    def generate_number(self):
        random_number = random.randint(0, 1000)
        self.ids.random_label.text = f"Random Number: {random_number}"  # Update label text


class NeutralRandom(App):
    def build(self):
        return MyRoot()


if __name__ == '__main__':
    neutral_random = NeutralRandom()
    neutral_random.run()