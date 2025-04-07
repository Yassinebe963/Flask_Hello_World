  etoiles = ''
    for j in range(valeur):
        for i in range(valeur-j):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles
