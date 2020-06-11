class Greeter:
    default = "World"
    # Class attributes can be initialized here

    def __init__(self, name):
        self.name = name
        # Instance attribute can be initialized here

    def __str__(self):
        return f"Greeter named {self.name}"

    def hello(self, target=None):
        if target is None:
            target = self.default
        print(f"Hello, {target}!")
        print(f"My name is {self.name}.")
        # Counts should be updated here, after hello does what it does normally

    def counts(self):
        # This should output the counts, using self as the reference to the specific Greeter
        pass


g1 = Greeter("John")
g2 = Greeter("Jane")
g1.hello()
g2.hello()
g2.hello()

# Should print "2 greeting(s) from Jane, 3 greeting(s) total"
g2.counts()
