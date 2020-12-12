def tags(value: str):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return f"<{value}>{result}</{value}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
