lista = ['A', 'B', 'C', 'D']

def pinta(valor):
    print(valor)
    return valor 

listaFunciones = []
listaIds = []
listaIdsFunciones = []

for text in lista:
    listaFunciones.append(lambda: pinta(text))  #Coge el valor de lo que valga text cuando se ejecuta lambda, no con el valor de la lista. Por eso en listaFunciones[0] se quedaría con D
            #Con lambda siempre va a interpretar el último valor
    listaIds.append(id(text))
    listaIdsFunciones.append(id(listaFunciones[-1]))

print(listaFunciones)