from functools import wraps


def debug(f):
    @wraps(f)
    def debug_wrapper(*args, **kwargs):
        print(f"{f.__name__} called with arguments:", *args, **kwargs)
        return f(*args, **kwargs)
    return debug_wrapper


def memoize(f):
    cache = {}  # Some sort of data structure to store cached results.
    # A dict works well, mapping { n: f(n) }

    @wraps(f)
    def memoize_wrapper(n):
        # Should check if result of f(n) is already computed
        # If not, compute, store and return
        # If yes, return stored

        # if n is in cache's keys:
        #     return cache[n]
        # else:
        #     compute f(n)
        #     store in cache[n]
        #     return it

        return f(n)
    return memoize_wrapper


@debug
def fib(n):
    if n in [0, 1]:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


@memoize
@debug
def memo_fib(n):
    if n in [0, 1]:
        return 1
    else:
        return memo_fib(n - 2) + memo_fib(n - 1)


print(f"f(6) is {fib(6)}")  # Logs 25 calls

print(f"f(6) is {memo_fib(6)}")  # Should log only 7 calls

print(f"f(5) is {memo_fib(5)}")  # Should log no calls: already calculated
