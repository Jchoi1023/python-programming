# CIS41 Jihye Choi
# Iterators and Generators

def fibonacci_function(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence

print(fibonacci_function(10))

'''
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''