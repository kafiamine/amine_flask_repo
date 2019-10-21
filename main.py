#"""ce fichier de test de la librairie flask"""
from flask import Flask
APP = Flask(__name__)
@APP.route('/')
def hello():
    """fonction d'affichage basic"""
    return 'hello world'
if __name__ == '__main__':
    APP.run(host="0.0.0.0")
