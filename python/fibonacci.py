memory = {1: 1, 2: 1}

n = int(input())

def fibonacci(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibonacci(n-1) + fibonacci(n-2)
        memory[n] = number
    return number

print(fibonacci(n))
