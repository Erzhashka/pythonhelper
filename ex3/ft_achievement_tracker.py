print("=== Achievement Tracker System ===\n")

alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
charlie = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'])

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}\n")

print("\n=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}\n")

common_all = alice.intersection(bob).intersection(charlie)
print(f"Common to all players: {common_all}")

rare = set()
for achievement in all_achievements:
    count = 0
    if achievement in alice:
        count = count + 1
    if achievement in bob:
        count = count + 1
    if achievement in charlie:
        count = count + 1
    if count == 1:
        rare = rare.union(set([achievement]))
print(f"Rare achievements (1 player): {rare}")

alice_bob_common = alice.intersection(bob)
print(f"Alice vs Bob common: {alice_bob_common}")

alice_unique = alice.difference(bob)
print(f"Alice unique: {alice_unique}")
