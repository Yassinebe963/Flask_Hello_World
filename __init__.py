n = int(input("Entrez un nombre n : "))
somme = 0

for nombre in range(1, n + 1):
    # Si divisible par 11, on passe au suivant
    if nombre % 11 == 0:
        continue
    
    # Si divisible par 5 ou 7
    if nombre % 5 == 0 or nombre % 7 == 0:
        # Vérifie si l'ajout dépasserait 5000
        if somme + nombre > 5000:
            break  # Arrêt immédiat sans ajouter
        somme += nombre  # Ajout sécurisé

print(f"Somme finale (≤ 5000) : {somme}")
