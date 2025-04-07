n = 5
for i in range(1, n + 1):
    # Espaces à gauche pour centrer
    print(' ' * (n - i), end='')
    
    # Partie croissante (1 à i)
    for j in range(1, i + 1):
        print(j, end='')
    
    # Partie décroissante (i-1 à 1)
    for j in range(i - 1, 0, -1):
        print(j, end='')
    
    # Nouvelle ligne
    print()
