from tkinter import *
from tkinter import ttk

dbuttons = [
    {
        'text': '1',
        'col': 0,
        'row': 4
    },
    {
        'text': '2',
        'col': 1,
        'row': 4
    },
    {
        'text': '3',
        'col': 2,
        'row': 4
    },
    {
        'text': '+',
        'col': 3,
        'row': 4
    },
    {
        'text': '4',
        'col': 0,
        'row': 3
    },
    {
        'text': '5',
        'col': 1,
        'row': 3
    },
    {
        'text': '6',
        'col': 2,
        'row': 3
    },
    {
        'text': '-',
        'col': 3,
        'row': 3
    },
    {
        'text': '7',
        'col': 0,
        'row': 2
    },
    {
        'text': '8',
        'col': 1,
        'row': 2
    },
    {
        "text": '9',
        'col': 2,
        'row': 2
    },
    {
        'text': 'x',
        'col': 3,
        'row': 2
    },
    {
        'text': 'C',
        'col': 1,
        'row': 1
    },
    {
        'text': '+/-',
        'col': 2,
        'row': 1
    },
    {
        'text': '÷',
        'col': 3,
        'row': 1
    },
    {
        'text': '0',
        'col': 0,
        'row': 5,
        'W': 2
    },
    {
        'text': ',',
        'col': 2,
        'row': 5
    },
    {
        'text': '=',
        'col': 3,
        'row': 5
    }
]

class Controlator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=300)  #(self, parent, width=272, height=300) Podemos eliminar las medidas, ya que hemos especificado en MainApp fill=BOTH
        d = Display(self)
        d.grid(column=0, row=0, columnspan=4)

        for properties in dbuttons:
            btn = CalcButton(self, properties['text'], command=, properties.get('W', 1), properties.get('H', 1))
            btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get('W', 1), rowspan=properties.get('H', 1))  
            '''
            if properties['text'] == '0':
                btn.pack_propagate(1)
                btn.grid(column=properties['col'], row=properties['row'], colspan=2)
            else:
                btn.grid(column=properties['col'], row=properties['row'])
'''

class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)
    
        s = ttk.Style()  #Crea una instancia de un estilo
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        lbl = ttk.Label(self, text='0', anchor=E, style='my.TLabel') #E = East/Derecha
        lbl.pack(side=TOP, fill=BOTH, expand=True)

class Selector(ttk.Radiobutton):
    pass

class CalcButton(ttk.Frame):
    def __init__(self, parent, value, command, width=1, heigth=1):
        ttk.Frame.__init__(self, parent, width=68*width, height=50*heigth)  #68 es 272/4
        self.pack_propagate(0)  #el pack_propagate(0) determina que el ancho se mantenga fijo

        btn = ttk.Button(self, text=value, command=command)    #creamos la instancia Button   #el valor del texto es value, heredado del __init__
        btn.pack(side=TOP, fill=BOTH, expand=True)  #Empaquetate arriba, rellena ambas dimensiones y expándete

'''
#Explicación de por qué no se utiliza self.value en la llamada al valor del  texto del boton:

class Persona():
    def __init__(self, nombre, apellidos, fecha_nac): # En el __init__ se hace la llamada a las variables locales
        self.nombre = nombre
        self.apellidos = apellidos  #Seguidamente se convierten las variables locales/parámetros en atributos propias de la función 
        self.fecha_nac = fecha_nac
'''



