  etoiles = ''
    for j in range(valeur):
        for i in range(valeur-j):
            etoiles += '+'   
        for k in range(j+1):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles

