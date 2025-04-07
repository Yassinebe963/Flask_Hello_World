n = int(input("Entrez un nombre n : "))
somme = 0

for nombre in range(1, n + 1):
    # Condition 1: Passer au suivant si divisible par 11
    if nombre % 11 == 0:
        continue
    
    # Condition 2: Ajouter si divisible par 5 ou 7
    if nombre % 5 == 0 or nombre % 7 == 0:
        somme += nombre
    
    # Condition 3: Arrêter si somme > 5000
    if somme > 5000:
        print("La somme a dépassé 5000 !")
        break

print(f"La somme finale est : {somme}")
