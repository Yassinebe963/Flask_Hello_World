from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
    etoiles = ''
    for j in range(valeur):
        for i in range(valeur):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles
