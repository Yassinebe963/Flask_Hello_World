from flask import Flask

app = Flask(__name__)

@app.route('/<path:numbers>')
def find_min(numbers):
    try:
        # Convertir les segments en nombres
        numbers_list = [int(n) for n in numbers.split('/')]
        
        if not numbers_list:
            return "Aucun nombre fourni", 400
        
        # Trouver le minimum manuellement
        minimum = numbers_list[0]
        for num in numbers_list[1:]:
            if num < minimum:
                minimum = num
                
        return f"{minimum}"  # Retourne juste la valeur minimale
    
    except ValueError:
        return "Erreur: nombres invalides", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
