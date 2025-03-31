from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(value):
        etoiles += '*'
    return etoiles #comm
    for i in range(br):
        etoile = '15'
        return </br>


if __name__ == "__main__":
  app.run(debug=True)
