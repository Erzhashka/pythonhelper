#!/usr/bin/env python3

class plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days= days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self, days):
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height}cm, {self.days} days old")
        for _ in range(days - 1):
            self.grow()
            self.age()
        print(f"=== Day {days} ===")
        print(f"{self.name}: {self.height}cm, {self.days} days old")
        print(f"Growth this week: +{days - 1}cm")
    
plant1 = plant("Rose", 25, 30)
plant2 = plant("Sunflower", 80, 45)
plant3 = plant("Cactus", 15, 120)

plant1.get_info(7)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
plant2.get_info(10)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
plant3.get_info(3)