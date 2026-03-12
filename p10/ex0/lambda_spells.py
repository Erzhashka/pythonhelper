from typing import Any

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    return sorted(artifacts, key=lambda x: x['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    return list(filter(lambda m: m['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:

    return list(map(lambda s: f"* {s} *", spells))

def mage_stats(mages: list[dict]) -> dict:

    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    total_power = sum(map(lambda m: m['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }

def main() -> None:

    print("=== Lambda Sanctum ===")
    print()

    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'divination'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'offensive'},
        {'name': 'Healing Amulet', 'power': 78, 'type': 'restoration'},
        {'name': 'Shadow Cloak', 'power': 88, 'type': 'stealth'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")
    print()

    print("Testing power filter...")
    mages = [
        {'name': 'Eldrin', 'power': 95, 'element': 'fire'},
        {'name': 'Lyra', 'power': 82, 'element': 'water'},
        {'name': 'Zeph', 'power': 70, 'element': 'air'},
        {'name': 'Terra', 'power': 88, 'element': 'earth'}
    ]
    powerful_mages = power_filter(mages, 85)
    print(f"Mages with power >= 85: {[m['name'] for m in powerful_mages]}")
    print()

    print("Testing spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))
    print()

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")
    print()

    print("Lambda mastery demonstrated!")

if __name__ == "__main__":
    main()
