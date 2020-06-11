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


class PortableContainer(Item, Container):
    def __init__(self, name, price, weight, weight_limit):
        Container.__init__(self, name, weight_limit)
        self.own_price = price
        self.own_weight = weight

    @property
    def price(self):
        # This code should return the total of the own price of the PortableContainer and all of its contents
        pass

    @property
    def weight(self):
        # This code should return the total of the own weight of the PortableContainer and all of its contents
        pass


inventory = Container("Player inventory", 50)
inventory.add(Item("Plate armor", 300, 25))
bag = PortableContainer("Bag", 1, 0.5, 15)
bag.add(Item("Mythril chainmail", 600, 10))
inventory.add(bag)

print(inventory)
print("Inside:")
for item in inventory:
    print(item)
