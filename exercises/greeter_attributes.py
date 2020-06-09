class Greeter:
    def hello(self, target="World"):
        print(f"Hello, {target}!")
        try:
            print(f"My name is {self.name}.")
        except AttributeError:
            print("I don't know my name yet.")


g = Greeter()

g.hello()
# Hello, World!
# I don't know my name yet.

g.name = "Fred"
g.hello("everyone")
# Hello, everyone!
# My name is Fred.
