n = int(input("10 : "))

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    # Partie montante
    for j in range(1, i + 1):
        print(j, end='')
    # Partie descendante
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()  # Retour à la ligne
