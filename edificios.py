import sys
#Las llaves son arreglos como texto, sus valores su computación
calculados = {}


def calcular(arreglo, k, char):
    #Obtiene el arreglo como cadena
    if len(arreglo) == 0:
        return (0,'')
    nombre = "".join(str(c) for c in arreglo)
    llave = (nombre,k)
    valor = calculados.get(llave)
    if valor != None:
        return valor
    
    edificioIzquierdo = arreglo[0]
    nuevoArregloIzq = arreglo[1:]
    tuplaIzq = calcular(nuevoArregloIzq,k+1,edificioIzquierdo)
    valorIzq = tuplaIzq[0] + edificioIzquierdo * k
    cadenaIzq = tuplaIzq[1]
    
    edificioDerecho = arreglo[len(arreglo)-1]
    nuevoArregloDer = arreglo[:len(arreglo)-1]
    tuplaDer = calcular(nuevoArregloDer,k+1,edificioDerecho)
    valorDer = tuplaDer[0] + edificioDerecho * k
    cadenaDer = tuplaDer[1]
    
    maximo = max(valorIzq, valorDer)
    #meter valor al diccionario
    if maximo == valorIzq:
        v = (valorIzq, (str(edificioIzquierdo) + "," + cadenaIzq))
        calculados[llave] = v
        return v
    else:
        v = (valorDer, (str(edificioDerecho) + "," + cadenaDer))
        calculados[llave] = v
        return v

if __name__ == "__main__":
    entrada = sys.argv[1]
    entrada = entrada[1:len(entrada)-1]
    entrada = entrada.split(",")
    for i in range(len(entrada)):
        entrada[i] = int(entrada[i])
    tuplaMax = calcular(entrada,1,'')
    valorMax = tuplaMax[0]
    cadenaMax = tuplaMax[1]
    cadenaMax = cadenaMax[0:len(cadenaMax)-1]
    print("valorMax: " + str(valorMax))
    print("cadenaMax: " + cadenaMax)