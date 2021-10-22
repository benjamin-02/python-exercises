def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a + b + c

a_function(10, 20, 30)
