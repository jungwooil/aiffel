x = int(input())

for i in range(x): 
    for j in reversed(range(x)):
        if j <= i:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(x):
        if j < i:
            print('*', end='')
        else:
            print(end='')
            
    print()

for i in range(1,x): 
    for j in range(x):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(x):
        if j > i:
            print('*', end='')
        else:
            print(end='')

            
    print()
