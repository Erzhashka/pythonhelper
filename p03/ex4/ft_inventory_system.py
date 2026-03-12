import sys

print("=== Inventory System Analysis ===")

if len(sys.argv) == 1:
    print("No items provided. Usage: python3 ft_inventory_system.py item:quantity ...")
else:
    inventory = dict()
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        item_name = parts[0]
        quantity = int(parts[1])
        inventory.update(dict([(item_name, quantity)]))
    
    total_items = 0
    for value in inventory.values():
        total_items = total_items + value
    
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    
    print("\n=== Current Inventory ===")
    sorted_items = []
    for item, qty in inventory.items():
        sorted_items = sorted_items + [(item, qty)]
    
    for i in range(len(sorted_items)):
        for j in range(i + 1, len(sorted_items)):
            if sorted_items[j][1] > sorted_items[i][1]:
                temp = sorted_items[i]
                sorted_items[i] = sorted_items[j]
                sorted_items[j] = temp
    
    for item, qty in sorted_items:
        percentage = (qty / total_items) * 100
        unit_word = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit_word} ({round(percentage, 1)}%)")
    
    print("\n=== Inventory Statistics ===")
    most_abundant = sorted_items[0]
    min_qty = sorted_items[len(sorted_items) - 1][1]
    least_abundant = None
    for item, qty in inventory.items():
        if qty == min_qty:
            least_abundant = (item, qty)
            break
    print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
    print(f"Least abundant: {least_abundant[0]} ({least_abundant[1]} unit)")
    
    print("\n=== Item Categories ===")
    moderate = dict()
    scarce = dict()
    for item, qty in inventory.items():
        if qty >= 5:
            moderate.update(dict([(item, qty)]))
        else:
            scarce.update(dict([(item, qty)]))
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    
    print("\n=== Management Suggestions ===")
    restock_list = []
    for item, qty in inventory.items():
        if qty == 1:
            restock_list = restock_list + [item]
    restock_str = ", ".join(restock_list)
    print(f"Restock needed: {restock_str}")
    
    print("\n=== Dictionary Properties Demo ===")
    keys_list = []
    for key in inventory.keys():
        keys_list = keys_list + [key]
    print(f"Dictionary keys: {', '.join(keys_list)}")
    
    values_list = []
    for value in inventory.values():
        values_list = values_list + [str(value)]
    print(f"Dictionary values: {', '.join(values_list)}")
    
    sword_exists = inventory.get("sword") is not None
    print(f"Sample lookup - 'sword' in inventory: {sword_exists}")
