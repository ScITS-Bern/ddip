class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.price} gold) [{self.weight} kg]"


class Container:
    def __init__(self, name, weight_limit):
        self.name = name
        self.weight_limit = weight_limit
        self._items = set()

    def items_weight(self):
        return sum(item.weight for item in self._items)

    def items_price(self):
        return sum(item.price for item in self._items)

    def can_add(self, item):
        if not isinstance(item, Item):
            raise ValueError("Containers can only contain Items")
        return self.items_weight() + item.weight <= self.weight_limit

    def add(self, item):
        if item in self._items:
            return
        if self.can_add(item):
            self._items.add(item)
        else:
            raise RuntimeError(f"Can't add {item} to {self}: over weight limit")

    def remove(self, item):
        self._items.remove(item)
        return item

    def clear(self):
        items = list(self._items)
        self._items.clear()
        return items

    def __str__(self):
        return f"{self.name} [{self.items_weight()}/{self.weight_limit} kg]"

    def __iter__(self):
        return self._items.__iter__()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def best_weapon(self):
        best_candidate = None
        for item in self._items:
            if isinstance(item, Weapon):
                if best_candidate is None:
                    best_candidate = item
                elif best_candidate.dps < item.dps:
                    best_candidate = item
        return best_candidate


class Weapon(Item):
    def __init__(self, name, price, weight, dps):
        super().__init__(name, price, weight)
        self.dps = dps

    def __str__(self):
        return super().__str__() + f" {{{self.dps} DPS}}"


sword = Weapon("Broadsword", 50, 5, 10)
print(sword)

inventory = Container("Player inventory", 50)

inventory.add(sword)
inventory.add(Weapon("Bow", 20, 4, 8))
inventory.add(Weapon("Battle axe", 70, 10, 15))

print(inventory)
for item in inventory:
    print(item)

print(inventory.best_weapon())  # Should be the item for Battle axe

chest = Container("Treasure chest", 30)
print(chest.best_weapon())  # Should print None
