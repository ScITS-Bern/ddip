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

    def loot(self, container):
        # This is just one, non-optimal solution that's better than the naive one in the hints - sorting by price-per-kilo.
        # I really encourage you to experiment and/or read up on the knapsack problem to truly optimize it.
        for item in sorted(container, key=lambda item: item.price / item.weight, reverse=True):
            if self.can_add(item):
                container.remove(item)
                self.add(item)


hoard = Container("Dragon's hoard", 1000)
hoard.add(Item("Rusty bucket", 0.1, 1))
hoard.add(Item("Large diamond", 1000, 0.1))
hoard.add(Item("Huge gold nugget", 10000, 100))
hoard.add(Item("Plate armor", 300, 25))
hoard.add(Item("Plate armor", 300, 25))
hoard.add(Item("Plate armor", 300, 25))
hoard.add(Item("Mythril chainmail", 600, 10))
hoard.add(Item("Mythril chainmail", 600, 10))
hoard.add(Item("Golden crown", 500, 4))
hoard.add(Item("Golden crown", 500, 4))
hoard.add(Item("Golden crown", 500, 4))
hoard.add(Item("Golden crown", 500, 4))
hoard.add(Item("Golden crown", 500, 4))
hoard.add(Item("Golden crown", 500, 4))
hoard.add(Item("Ornate statue", 700, 40))
hoard.add(Item("Potion of healing", 100, 0.2))
hoard.add(Item("Potion of healing", 100, 0.2))
hoard.add(Item("Potion of healing", 100, 0.2))
hoard.add(Item("Potion of healing", 100, 0.2))
hoard.add(Item("Potion of healing", 100, 0.2))
hoard.add(Item("Potion of healing", 100, 0.2))
hoard.add(Item("Potion of strength", 300, 0.4))

inventory = Container("Player inventory", 50)
inventory.loot(hoard)

print(inventory)
for item in inventory:
    print(f"> {item}")
print(f"Total looted value: {inventory.items_price()} gold")
# Can you get this over 6000?
