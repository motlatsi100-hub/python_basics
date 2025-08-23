# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 16:28:27 2025

@author: motlatsi seeko
"""

# Parent Class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery   # encapsulation (private attribute)

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} ")

    def charge(self, amount):
        self.__battery += amount
        print(f"{self.brand} {self.model} charged. Battery now {self.__battery}% ")

    def get_battery(self):
        return self.__battery

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model}  with {self.cooling_system} cooling system")
