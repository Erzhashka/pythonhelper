#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height, age):
        self.__name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, value):
        if value >= 0:
            self.__height = value
        else:
            print(f"Error: Height cannot be negative ({value})")

    def set_age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print(f"Error: Age cannot be negative ({value})")

    def grow(self):
        self.__height += 1

    def age_up(self):
        self.__age += 1

    def get_info(self):
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"


# Test the SecurePlant
print("=== Creating plants ===")
plant1 = SecurePlant("Rose", 25, 30)
plant2 = SecurePlant("Sunflower", 80, 45)

print(plant1.get_info())
print(plant2.get_info())

print("\n=== Trying invalid values ===")
plant1.set_height(-10)
plant1.set_age(-5)

print("\n=== Valid modifications ===")
plant1.set_height(30)
plant1.grow()
print(plant1.get_info())

print("\n=== Trying direct access (will fail) ===")
try:
    print(plant1.__height)
except AttributeError as error_message:
    print(f"Cannot access private data: {error_message}")

print(plant1._SecurePlant__height)