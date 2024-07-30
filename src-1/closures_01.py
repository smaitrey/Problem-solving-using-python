"""
A closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory.
Key Points of Closures:
    1. Nested Function: There must be a nested function (a function inside another function).
    2. Enclosing Scope: The nested function must refer to a variable defined in the enclosing scope.
    3. Function Returned: The enclosing function must return the nested function.

The outer_function returns the inner_function, which forms a closure.
function encapsulation
Closures can be used as callback function, provides some sort of data hiding, reduces the use of global variables.
Closures can be used to avoid needless use of class.

"""

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

# Create a closure
closure_1 = outer_function("Hello")
closure_2 = outer_function("World")

# Call the closure
closure_1()  # Output: Hello
closure_2()  # Output: World


## Let's create a closure that maintains state.
def make_counter():
    count = 0  # This variable will be captured by the closure

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# Create a closure instance
counter1 = make_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1())  # Output: 3

# Create another closure instance
counter2 = make_counter()

print(counter2())  # Output: 1
print(counter2())  # Output: 2

## Closures are often used in decorators to enhance the functionality of existing functions.
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

# Create different greeters
hello_greeter = make_greeter("Hello")
hi_greeter = make_greeter("Hi")

# Use the greeters
print(hello_greeter("Alice"))  # Output: Hello, Alice!
print(hi_greeter("Bob"))       # Output: Hi, Bob!

## Memoization with Closures
def memoize(f):
    cache = {}

    def memoized_function(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return memoized_function

# Example usage
@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
print(factorial(6))  # Output: 720, calculated using the cached value of factorial(5)

"""
In this example, memoize is a decorator that creates a closure. The closure maintains a cache dictionary to store results of function calls.
The memoized_function checks if the result is already in the cache; if not, it computes and stores it.
"""


