# Filename: main.py
# Author: inter5tellar
# Description: Imports dictionaries from deck_dict.py. Uses tarot.kv to create GUI.

import kivy
kivy.require('2.1.0')

from deck_dict import deck

import keyboard
import random

from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


Window.size = (650, 450)
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'top', '200')
Config.set('graphics', 'left', '430')
Config.set('graphics', 'position', 'custom')
Config.write()


class Tarot(FloatLayout):
    # fields
    image_location = StringProperty('roses.png')
    image_location2 = StringProperty('roses.png')
    image_location3 = StringProperty('roses.png')
    card_name = StringProperty("")
    card_name2 = StringProperty("")
    card_name3 = StringProperty("")
    name = ObjectProperty(None)
    pw = ObjectProperty(None)
    logged_in = False

    users = {'key': 'value'}

    # TODO
    # while logged_in:
        # display name

    # Draw and display the appropriate amount of cards
    # If user is logged in, store card pull history in journal
    # TODO Make Iterative/Recursive to cut down coding
    def draw_card(self, draws):
        # If Pick 1 is clicked, reset cards 2 & 3
        if draws == 1:
            self.card_name2 = ""
            self.card_name3 = ""
            self.image_location2 = 'roses.png'
            self.image_location3 = 'roses.png'

        # If either Pick 1 or Pick 3 is clicked, draw one card
        drawn_card = random.choice(deck)
        if drawn_card.get('suit') == 'none':
            self.card_name = drawn_card.get('name')
        else:
            self.card_name = drawn_card.get('name') + " of " + drawn_card.get('suit')
        self.image_location = drawn_card.get('image')

        # If Pick 3 is clicked, draw 2 additional cards
        if draws == 3:
            drawn_card2 = random.choice(deck)
            if drawn_card2.get('suit') == 'none':
                self.card_name2 = drawn_card2.get('name')
            else:
                self.card_name2 = drawn_card2.get('name') + " of " + drawn_card2.get('suit')
            self.image_location2 = drawn_card2.get('image')

            drawn_card3 = random.choice(deck)
            if drawn_card3.get('suit') == 'none':
                self.card_name3 = drawn_card3.get('name')
            else:
                self.card_name3 = drawn_card3.get('name') + " of " + drawn_card3.get('suit')
            self.image_location3 = drawn_card3.get('image')

    # Show the journal (log of card pulls) if logged in
    # If not, prompt to log in
    def view_journal(self):
        if self.logged_in:
            print("Journal")
        else:
            print("Sign in to view journal")

    # Log user in or create new user when 'Log in' button is clicked
    def login_button(self):
        if self.name.text in self.users:
            value = self.users[self.name.text]
            if value == self.pw.text:
                print(self.name.text, " successfully logged in")
                self.name.text = ""
                self.pw.text = ""
                self.logged_in = True
            else:
                print("Incorrect password")
                self.pw.text = ""
        else:
            print("This user does not exist, create it now? Y or N")
            while True:
                if keyboard.is_pressed('y'):
                    self.users.update({self.name.text: self.pw.text})
                    print("User ", self.name.text, " created. Log in now")
                    self.name.text = ""
                    self.pw.text = ""
                    break
                elif keyboard.is_pressed('n'):
                    self.name.text = ""
                    self.pw.text = ""
                    break


# alternate way to load .kv
# layout = Builder.load_file('tarot.kv')


class TarotApp(App):
    def build(self):
        return Tarot()


if __name__ == '__main__':
    TarotApp().run()
