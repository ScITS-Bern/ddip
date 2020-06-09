from functools import wraps


def debug(f):
    @wraps(f)
    def debug_wrapper(*args, **kwargs):
        print(f"{f.__name__} called with arguments:", *args, **kwargs)
        return f(*args, **kwargs)
    return debug_wrapper


def memoize(f):
    # YOUR CODE HERE
    @wraps(f)
    def memoize_wrapper(n):
        # YOUR CODE HERE
        pass
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
