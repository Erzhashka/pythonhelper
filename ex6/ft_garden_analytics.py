#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth_total = 0

    def grow(self):
        self.height += 1
        self.growth_total += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True

    def get_info(self):
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status}), Prize points: {self.prize_points}"


class GardenManager:
    garden_count = 0

    class GardenStats:
        @staticmethod
        def count_by_type(plants):
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                if type(plant) == PrizeFlower:
                    prize += 1
                elif type(plant) == FloweringPlant:
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def total_growth(plants):
            total = 0
            for plant in plants:
                total += plant.growth_total
            return total

        @staticmethod
        def calculate_score(plants):
            score = 0
            for plant in plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 4
            return score

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.plants_added = 0
        GardenManager.garden_count += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self):
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
        print()

    def get_report(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print()
        
        total_growth = self.GardenStats.total_growth(self.plants)
        print(f"Plants added: {self.plants_added}, Total growth: {total_growth}cm")
        
        regular, flowering, prize = self.GardenStats.count_by_type(self.plants)
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls, owner_names):
        gardens = []
        for name in owner_names:
            gardens.append(cls(name))
        return gardens

    @classmethod
    def get_total_gardens(cls):
        return cls.garden_count

    @staticmethod
    def validate_height(height):
        return height >= 0


print("=== Garden Management System Demo ===")
print()

alice_garden = GardenManager("Alice")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
rose.bloom()
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
sunflower.bloom()

alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)
print()
alice_garden.grow_all()
alice_garden.get_report()
print()

print(f"Height validation test: {GardenManager.validate_height(50)}")

# Create Bob's garden silently for score comparison
bob_garden = GardenManager("Bob")
bob_garden.plants = [Plant("Fern", 50), FloweringPlant("Daisy", 42, "white")]

alice_score = GardenManager.GardenStats.calculate_score(alice_garden.plants)
bob_score = GardenManager.GardenStats.calculate_score(bob_garden.plants)
print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
