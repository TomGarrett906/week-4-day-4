'''
Exercise 2: Count Function Calls

Decorators can also be used to modify the behavior of functions in other ways, such as tracking how many times they have been called. In this exercise, you will write a decorator that counts the number of times a function has been invoked.

1. Create the Decorator: Write a decorator called `count_calls` that will increment a counter each time the decorated function is invoked.
    - You may want to use nonlocal variables or attributes on the function object to keep track.
 
2. Apply to Fibonacci: Add the `count_calls` decorator to your memoized Fibonacci function from Exercise 1.
 
3. Test the Count: Run the decorated function several times and verify that the count is accurate.
'''

def counter(func):
    count = 0

    def inner(*args):

        nonlocal count
        count += 1
        result = func(*args)
        return result
    inner.counter = counter
    return inner


@counter
# Fibanacci funtion
def fib(num):
    
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


print(fib(20))