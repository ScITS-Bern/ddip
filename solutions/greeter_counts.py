class Greeter:
    default = "World"
    total_count = 0  # Class attribute: shared among all

    def __init__(self, name):
        self.name = name
        self.count = 0  # Instance attribute: unique to one

    def __str__(self):
        return f"Greeter named {self.name}"

    def hello(self, target=None):
        if target is None:
            target = self.default
        print(f"Hello, {target}!")
        print(f"My name is {self.name}.")
        self.count += 1
        Greeter.total_count += 1  # Needs to be accessed through the class name for assignment

    def counts(self):
        print(f"{self.count} greeting(s) from {self.name}, {self.total_count} greeting(s) total")


g1 = Greeter("John")
g2 = Greeter("Jane")
g1.hello()
g2.hello()
g2.hello()

# Should print "2 greeting(s) from Jane, 3 greeting(s) total"
g2.counts()
