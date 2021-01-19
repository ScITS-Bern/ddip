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
        self._counts = {}  # A dict that maps an Item to its count inside

    def count(self, item):
        return self._counts.get(item, 0)

    def items_weight(self):
        return sum(item.weight * self.count(item) for item in self._counts)

    def items_price(self):
        return sum(item.price * self.count(item) for item in self._counts)

    def can_add(self, item):
        if not isinstance(item, Item):
            raise ValueError("Containers can only contain Items")
        return self.items_weight() + item.weight <= self.weight_limit

    def add(self, item):
        if self.can_add(item):
            self._counts[item] = self.count(item) + 1
        else:
            raise RuntimeError(f"Can't add {item} to {self}: over weight limit")

    def remove(self, item):
        if self.count(item) > 0:
            self._counts[item] = self.count(item) - 1
        else:
            raise KeyError(f"Item {item} not found in {self}")

        return item

    def __iter__(self):
        for item in self._counts:
            for i in range(self.count(item)):
                yield item

    def __len__(self):
        return sum(self.count(item) for item in self._counts)

    def __contains__(self, item):
        return self.count(item) > 0

    def __str__(self):
        return f"{self.name} [{self.items_weight()}/{self.weight_limit} kg]"

    def best_weapon(self):
        # YOUR CODE HERE
        pass


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
inventory.add(Weapon("Battle axe", 70, 10, 15))
inventory.add(Weapon("Bow", 20, 4, 8))

print(inventory)
for item in inventory:
    print(f"> {item}")

print(f"Best weapon in inventory is {inventory.best_weapon()}")  # Should be the item for Battle axe

chest = Container("Treasure chest", 30)
chest.add(Item("Potion of healing", 100, 0.2))
print(f"Best weapon in chest is {chest.best_weapon()}")  # Should print None
