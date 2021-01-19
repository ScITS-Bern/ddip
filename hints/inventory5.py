class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.price} gold) [{self.weight} kg]"


class ContainerImmutable:
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

    def _add(self, item):
        # It's a good idea to have the old method as well: we need it internally
        if self.can_add(item):
            self._counts[item] = self.count(item) + 1
        else:
            raise RuntimeError(f"Can't add {item} to {self}: over weight limit")

    def add(self, item):
        # Should return a new Container that has the item added, everything else the same
        # Do not modify self

        # You need a new_container, that has the same items and other properties
        # Make a new one then add all old items to it
        # Then add the new item and return the new container
        pass

    def remove(self, item):
        # This should also be modified, but not part of the exercise
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


inventory = ContainerImmutable("Player inventory", 50)
new_inventory = inventory.add(Item("Golden crown", 500, 4))

assert len(new_inventory) == 1
assert len(inventory) == 0
