def add_inventory(inventory, items):
    for item in items:
        inventory[item] = inventory.setdefault(item, 0) + 1
    

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('{0} {1}'.format(v, k))
        item_total += v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_inventory(inv, dragonLoot)
display_inventory(inv)