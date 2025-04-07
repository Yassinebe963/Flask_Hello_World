from flask import Flask

app = Flask(__name__)

@app.route('/<path:numbers>')
def find_max(numbers):
    try:
        # Convertir les segments en nombres
        numbers_list = [int(n) for n in numbers.split('/')]
        
        if not numbers_list:
            return "Aucun nombre fourni", 400
        
        # Trouver le maximum manuellement
        maximum = numbers_list[0]
        for num in numbers_list[1:]:
            if num > maximum:
                maximum = num
                
        return f"Le maximum parmi {numbers_list} est {maximum}"
    
    except ValueError:
        return "Tous les segments doivent être des nombres valides", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
