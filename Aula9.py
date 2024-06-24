def soma(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

x = soma(2, 3, 4, 5, 6)
print(x)
