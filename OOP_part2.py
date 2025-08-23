# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 16:34:07 2025

@author: motlatsi seeko
"""

class Animal:
    def move(self):
        print("The animal moves in some way")

class Dog(Animal):
    def move(self):
        print("Dog is running ")

class Bird(Animal):
    def move(self):
        print("Bird is flying ")

class Vehicle:
    def move(self):
        print("The vehicle moves on the road ")

class Car(Vehicle):
    def move(self):
        print("Car is driving ")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈")

# Polymorphism in action
objects = [Dog(), Bird(), Car(), Plane()]

for obj in objects:
    obj.move()   # Each one behaves differently!
