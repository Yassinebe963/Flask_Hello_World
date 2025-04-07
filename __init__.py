n = 5  # Vous pouvez modifier cette valeur ou demander à l'utilisateur

for i in range(1, n + 1):
    # Partie gauche (espaces + nombres croissants)
    ligne = ' ' * (n - i)  # Espaces pour centrer
    ligne += ''.join(str(j) for j in range(1, i + 1))  # 1 -> i
    
    # Partie droite (nombres décroissants)
    ligne += ''.join(str(j) for j in range(i - 1, 0, -1))  # i-1 -> 1
    
    print(ligne)  # Affiche la ligne complète
