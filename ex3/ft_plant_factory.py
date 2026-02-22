#!/usr/bin/env python3

class plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

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


plant_data = [
    ("Rose", 25, 30),
    ("Sunflower", 80, 45),
    ("Cactus", 15, 120),
    ("67flower", 67, 67),
    ("hello_world_flower", 5, 5)
]

plants = [plant(name, height, days) for name, height, days in plant_data]

print("=== Plant Factory Output ===")
for self in plants:
    print(f"Created: {self.name} ({self.height}cm, {self.days} days old)")
print("\n")
print(f"Total plants created: {len(plants)}")