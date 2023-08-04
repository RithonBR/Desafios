def primo(num, divisor=2):
    if num <= 1:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return primo(num, divisor + 1)

def primoRecursivo(N):
    if N <= 1:
        return []
    
    primoLs = primoRecursivo(N - 1)
    if primo(N):
        primoLs.append(N)
    
    return primoLs

def primoLinear(N):
    def primo(num):
        if num <= 1:
            return False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return False
        return True

    primoLs = [num for num in range(2, N + 1) if primo(num)]
    return primoLs

# Testando a função recursiva
print("Números Primos até 2:", primoRecursivo(2))
print("Números Primos até 3:", primoRecursivo(3))
print("Números Primos até 10:", primoRecursivo(10))

# Testando a função linear
print("Números Primos até 2:", primoLinear(2))
print("Números Primos até 3:", primoLinear(3))
print("Números Primos até 10:", primoLinear(10))
