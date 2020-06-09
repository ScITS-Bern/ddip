from mypackage.decorators.debug import debug
from mypackage.snippets.hello import hello
from mypackage.snippets import default_target as default


@debug
def new_hello(target=default):
    hello(target)


new_hello()
