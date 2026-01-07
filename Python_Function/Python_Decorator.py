# Decorators let you add extra behavior to a function, without changing the function's code.


#Basic Decorator
#Define the decorator first, then apply it with @decorator_name above the function.

def add_last_name(func):
    def add_name():
        return func() + "Rahaman"
    return add_name


@add_last_name
def print_full_name():
    return "Ashikur "

print(print_full_name())
