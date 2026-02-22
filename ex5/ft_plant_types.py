#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"

    def produce_shade(self):
        shade_area = self.height * self.trunk_diameter // 100
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"

    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


print("=== Garden Plant Types ===")
print()
# Flowers
rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 20, 14, "yellow")

print(rose.get_info())
rose.bloom()
print()
print(tulip.get_info())
tulip.bloom()

print()

# Trees
oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 400, 1460, 35)

print(oak.get_info())
oak.produce_shade()
print()
print(pine.get_info())
pine.produce_shade()

print()

# Vegetables
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 70, "fall", "vitamin A")

print(tomato.get_info())
tomato.show_nutrition()
print()
print(carrot.get_info())
carrot.show_nutrition()
