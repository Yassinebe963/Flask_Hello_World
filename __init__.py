from flask import Flask

app = Flask(__name__)

@app.route('/<path:numbers>')
def find_min_max(numbers):
    try:
        # Conversion des segments en nombres
        numbers_list = [int(n) for n in numbers.split('/')]
        
        if not numbers_list:
            return "Aucun nombre fourni", 400
        
        # Initialisation du min et max avec le premier nombre
        minimum = maximum = numbers_list[0]
        
        # Recherche du min et max
        for num in numbers_list[1:]:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
                
        return (
            f"Nombres analysés: {numbers_list}<br>"
            f"Minimum: {minimum}<br>"
            f"Maximum: {maximum}"
        )
    
    except ValueError:
        return "Erreur: Tous les segments doivent être des nombres valides", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
