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
        # Should return a new Container that has the item added, everything else the same
        # Do not modify self

        # You need a new_container, that has the same items and other properties
        # Make a new one then add all items to it

        if item in self._items:
            # Nothing to add: return new Container as-is
            return
        if self.can_add(item):
            # Add to new container then return
            return
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


inventory = Container("Player inventory", 50)
new_inventory = inventory.add(Item("Golden crown", 500, 4))

assert len(new_inventory) == 1
assert len(inventory) == 0
