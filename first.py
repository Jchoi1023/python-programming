# print("\"Hello World\"")
# Review the code snippet below:
# i = 1
# while i <= 10:
#     print('d')
#     i = i + 10
# a = input("D")
# b = input("s")
# print(a+b)

def fibonacci_function(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence

print(fibonacci_function(10))