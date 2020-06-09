from functools import wraps


def debug(f):
    @wraps(f)
    def debug_wrapper(*args, **kwargs):
        print(f"{f.__name__} called with arguments:", *args, **kwargs)
        return f(*args, **kwargs)
    return debug_wrapper
