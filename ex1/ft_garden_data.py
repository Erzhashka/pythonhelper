#!/usr/bin/env python3

class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

plant1 = plant("Rose", 25, 30)
plant2 = plant("Sunflower", 80, 45)
plant3 = plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old ")
print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old ")
print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old ")