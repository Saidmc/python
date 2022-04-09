def es_primo(x):
    for i in range(2,x):
        if not(x%i):
            return False

    return True

for i in range(1,101):
    if es_primo(i):
        print(f'{i} es primo')