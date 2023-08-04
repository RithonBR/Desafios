def fibonnaciRecursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaciRecursivo(n - 1) + fibonnaciRecursivo(n - 2)

def fibonnaciLinear(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fibAntes, fibAtual = 0, 1
    for _ in range(2, n + 1):
        fibAntes, fibAtual = fibAtual, fibAntes + fibAtual

    return fibAtual

# Testando a função recursiva
print(f"Fibonacci(0) = {fibonnaciRecursivo(0)}")
print(f"Fibonacci(1) = {fibonnaciRecursivo(1)}")
print(f"Fibonacci(2) = {fibonnaciRecursivo(2)}")
print(f"Fibonacci(3) = {fibonnaciRecursivo(3)}")
print(f"Fibonacci(5) = {fibonnaciRecursivo(5)}")
print(f"Fibonacci(6) = {fibonnaciRecursivo(6)}")

# Testando a função linear
print(f"Fibonacci(0) = {fibonnaciLinear(0)}")
print(f"Fibonacci(1) = {fibonnaciLinear(1)}")
print(f"Fibonacci(2) = {fibonnaciLinear(2)}")
print(f"Fibonacci(3) = {fibonnaciLinear(3)}")
print(f"Fibonacci(5) = {fibonnaciLinear(5)}")
print(f"Fibonacci(6) = {fibonnaciLinear(6)}")
