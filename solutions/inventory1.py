class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.price} gold) [{self.weight} kg]"


potion = Item("Potion of healing", 100, 0.2)
print(f"potion is {potion}")


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
        # Should remove Item "item" from the Container "self" and return it
        # Raise an error if it's not in the Container
        if self.count(item) > 0:
            self._counts[item] = self.count(item) - 1
        else:
            raise KeyError(f"Item {item} not found in {self}")

        return item  # If we need to return something, it's "item"

    def __str__(self):
        return f"{self.name} [{self.items_weight()}/{self.weight_limit} kg]"


inventory = Container("Player inventory", 50)
inventory.add(potion)
print(inventory)

# Should output item for "Potion of healing"
print(f"(1) Removed item {inventory.remove(potion)}")

# Should raise an exception
print(f"(2) Removed item {inventory.remove(potion)}")
