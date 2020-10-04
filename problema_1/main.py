a = [1, 1, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0]
b = [1, 1, 1, 0, 2, 1, 0, 0, 2, 0, 0, 0, 1]
c = [0, 2, 2, 2, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0]
d = [3, 3, 3, 3, 3, 3, 3, 1, 0, 0, 0, 1]

#Inicializamos nuestra lista de objetos regador
def inicia(x):

    lista = []
    for i, val in enumerate(x):
        anterior = i-val
        posterior = i+val
        if anterior < 0:
            anterior = 0
        aux = []
        for j in range(anterior, (posterior+1)):
            aux.append(j)

        reg = Regador(aux,i)
        lista.append(reg)

    return lista

#Calcula todos los caminos posibles
def camino(reg, lista):
    caminos_sgt = sgt_camninos(reg, lista)
    caminos = []
    if caminos_sgt:
        for c in caminos_sgt:
            x = camino(c, lista)
            for val in x:
                val.append(reg.indice)
                caminos.append(val)

    else:
        caminos.append([reg.indice])

    return caminos

#Detecta los primeros regadores , es decir los que estan en la posicion 0
def caminos_iniciales(lista):
    camino_inicio = []
    for reg in lista:
        if reg.espacio[0] == 0:
            camino_inicio.append(reg)
    return camino_inicio

#Calcula los posibles siguientes regadores que pueden cubrir mas areas respecto al regador que se ingrese como parametro
def sgt_camninos(reg, lista):

    caminos = intersecciones(reg, lista)+consecutivo(reg, lista)

    return caminos

#Calcula el mejor camino
def mejor_camino(lista):

    min = len(lista[0])
    mejores = []
    for val in lista:
        aux = len(val)
        if aux < min:
            min = aux

    for val in lista:
        if len(val) == min:
            mejores.append(val)

    return mejores

#Calcula los regadores q pueden regar una misma area
def intersecciones(reg, lista):
    x = set(reg.espacio)
    aux = []
    for regador in lista:
        if regador.indice > reg.indice:
            y = set(regador.espacio)
            if x.intersection(y):
                aux.append(regador)
    return aux

#un regador puede regar un espacio maximo , y su consecutivo a ese maximo seria un regador en su minimo sea el maximo del anterior
#Esta funcion calcula un siguiente regador con respecto al espacio que cubre
def consecutivo(reg, lista):
    x = reg.espacio[-1]
    aux = []
    for regador in lista:
        if regador.indice > reg.indice:
            y = regador.espacio[0]
            if (x+1) == y:
                aux.append(regador)

    return aux


def run():

    """PARA EL ARRAY A"""
    #se recorre el arregle creando un lista de objetos Regador
    lista = inicia(a)
    #obtenemos los regadores iniciales , es decir aquellos que tengan la posicion 0 del arreglo
    inicios = caminos_iniciales(lista)
    #caminos almacenara todas las posibles combinaciones que tienen como inicio la posicion 0
    caminos = []
    for inicio in inicios:
        rutas = camino(inicio, lista)
        caminos += rutas
    #Se halla las mejores combinaciones, aquella que no tengan muchos elementos
    mejor = mejor_camino(caminos)
    print("PARA EL ARRAY A")
    print("Se tienen {} solucion(es)".format(str(len(mejor))))
    print("Se debe encender {} regador(es)".format(str(len(mejor[0]))))
    for val in mejor:
        separator=','.join(str(num) for num in val)
        print("posiciones de los regadores que se debe encender:",separator)
    print("-----------------------------------------------------------------------")
    """PARA EL ARRAY B"""
    lista = inicia(b)
    inicios = caminos_iniciales(lista)
    caminos = []
    for inicio in inicios:
        rutas = camino(inicio, lista)
        caminos += rutas
    mejor = mejor_camino(caminos)
    print("PARA EL ARRAY B")
    print("Se tienen {} solucion(es)".format(str(len(mejor))))
    print("Se debe encender {} regador(es)".format(str(len(mejor[0]))))
    for val in mejor:
        separator=','.join(str(num) for num in val)
        print("posiciones de los regadores que se debe encender:",separator)
    print("----------------------")
    """PARA EL ARRAY C"""
    lista = inicia(c)
    inicios = caminos_iniciales(lista)
    caminos = []
    for inicio in inicios:
        rutas = camino(inicio, lista)
        caminos += rutas
    mejor = mejor_camino(caminos)
    print("PARA EL ARRAY C")
    print("Se tienen {} solucion(es)".format(str(len(mejor))))
    print("Se debe encender {} regador(es)".format(str(len(mejor[0]))))
    for val in mejor:
        separator=','.join(str(num) for num in val)
        print("posiciones de los regadores que se debe encender:",separator)
    print("----------------------")
    """PARA EL ARRAY D"""
    lista = inicia(d)
    inicios = caminos_iniciales(lista)
    caminos = []
    for inicio in inicios:
        rutas = camino(inicio, lista)
        caminos += rutas
    mejor = mejor_camino(caminos)
    print("PARA EL ARRAY D")
    print("Se tienen {} solucion(es)".format(str(len(mejor))))
    print("Se debe encender {} regador(es)".format(str(len(mejor[0]))))
    for val in mejor:
        separator=','.join(str(num) for num in val)
        print("posiciones de los regadores que se debe encender:",separator)
    print("----------------------")


class Regador():

    def __init__(self, espacio, indice):
        self.espacio = espacio
        self.indice = indice


if __name__ == "__main__":
    run()
