''' Instructions:

1. Write a Decorator: Create a Python decorator called `memoize` that will store already computed values for any function to which it's applied.
    - Use a dictionary to store the results.
    - The keys will be the arguments passed to the function, and the values will be the results.
 
2. Apply to Fibonacci: Apply the `memoize` decorator to a recursive Fibonacci function. The function should take an integer `n` and return the nth Fibonacci number.
 
3. Test It: Test your decorated Fibonacci function with high values of `n`.
    - For comparison, run the same function without the decorator and notice the speed difference.
    - Use your new unittest skills we learned today!
'''
def memoize(func):
    cache_dict = {}

    def inner(i):
        if i not in cache_dict:
            cache_dict[i] = func(i) 
            # print(cache_dict())
        return cache_dict[i]
    return inner
#decorator 
@memoize
# Fibanacci funtion
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

print(fib(200))


