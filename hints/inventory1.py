class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.price} gold) [{self.weight} kg]"


potion = Item("Potion of healing", 100, 0.2)
print(potion)


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
        # Should remove Item "item" from the Container "self" and return it
        # Raise an error if it's not in the Container

        # The items are stored in a set "self._items" - see the set() documentation for appropriate methods to use
        # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

        return item  # If we need to return something, it's "item"

    def clear(self):
        # Should remove all Items from the Container "self" and return them in any iterable

        # The items are stored in a set "self._items" - see the set() documentation for an appropriate method to use
        # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
        pass

    def __iter__(self):
        return self._items.__iter__()

    def __len__(self):
        # Implement "len(self)" by using "len(self._items)"
        pass

    def __contains__(self, item):
        # Implement "x in self" by using "x in self._items"
        pass

    def __str__(self):
        return f"{self.name} [{self.items_weight()}/{self.weight_limit} kg]"


inventory = Container("Player inventory", 50)
inventory.add(potion)
print(inventory)

inventory.add(Item("Plate armor", 300, 20))
inventory.add(Item("Large diamond", 1000, 0.1))

# Should output item for "Potion of healing"
print(inventory.remove(potion))
# Should output items for "Plate armor" and "Large diamond"
for item in inventory.clear():
    print(item)

# Should raise an exception
print(inventory.remove(potion))
