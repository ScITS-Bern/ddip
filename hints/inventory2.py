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
        # You have a Container "container" to find items from
        # Naive implementation would be trying every item and taking them if they still fit:
        for item in list(container):  # Using list(container) to get a copy of all items, because we'll be changing the container during iteration
            if self.can_add(item):
                container.remove(item)
                self.add(item)
        # However, this can fill your "self" container with worthless junk before pricy stuff can be added
        # Generally, this problem is known as the 0-1 knapsack problem: https://en.wikipedia.org/wiki/Knapsack_problem
        # There are many possible approaches of different complexity. A simpler one would be to sort items by something before trying to add them.
        # Using the sorted() function on "container" with appropriate key function and/or reverse flag will do that.
        # Documentation: https://docs.python.org/3/library/functions.html#sorted


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
