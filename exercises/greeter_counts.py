class Greeter:
    default = "World"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Greeter named {self.name}"

    def hello(self, target=None):
        if target is None:
            target = self.default
        print(f"Hello, {target}!")
        print(f"My name is {self.name}.")

    def counts(self):
        # ADD CODE HERE
        pass


g1 = Greeter("John")
g2 = Greeter("Jane")
g1.hello()
g2.hello()
g2.hello()

# Should print "2 greeting(s) from Jane, 3 greeting(s) total"
g2.counts()
