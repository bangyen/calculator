lista = ['A', 'B', 'C', 'D']

def pinta(valor):
    print(valor)
    return valor 

listaFunciones = []
listaIds = []
listaIdsFunciones = []

for text in lista:
    listaFunciones.append(lambda: pinta(text))
    listaIds.append(id(text))
    listaIdsFunciones.append(id(listaFunciones[-1]))

print(listaFunciones)