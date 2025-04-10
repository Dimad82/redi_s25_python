def factorial(n):
    if n == 1: 
        return
    return n * factorial(n - 1)


print("actual:", factorial(5))
print("expected:", 5 * 4 * 3 * 2 * 1)
print("actual == expected?", factorial(5) == 5 * 4 * 3 * 2 * 1)

# check factorial(2)
# check factorial(1)
# check factorial(0)


def fibonacci(n):
    """
    https://en.wikipedia.org/wiki/Fibonacci_number

    Calculate the nth Fibonacci number, e.g.
    fibonacci(10) = 55
    """
    a = 1
    b = 1

    for _ in range(1, n):
        a = b
        b = a + b

    return a


# print(fibonacci(10))
# check fibonacci(10)
# check fibonacci(5)
# check fibonacci(2)
# check fibonacci(1)
# check fibonacci(0)
