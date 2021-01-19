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

print(bag)
for item in bag:
    print(f"> {item}")

inventory.add(bag)

print(inventory)
for item in inventory:
    print(f"> {item}")
