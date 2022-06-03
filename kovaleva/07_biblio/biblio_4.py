def fib(n):
    a, b = 0, 1
    for ryad in range(n):
        yield a
        a, b = b, a + b

n = 10 # количество чисел в ряду
print(list(fib(n)))   