class Vehicle():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(Vehicle):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return 'Objeto de la clase: Coche. \nColor: {}.\nRuedas: {}.\nVelocidad : {} Km/h \nCilindrada: {} cc.\n'.format(self.color, self.ruedas, self.velocidad, self.cilindrada)


class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return 'Objeto de la clase: Camioneta. \nColor: {}.\nRuedas: {}.\nVelocidad : {} Km/h \nCilindrada: {} \nCarga: {} Kg.\n'.format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)


class Bicicleta(Vehicle):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return 'Objeto de la clase: Bicicleta. \nColor: {}.\nRuedas: {}.\nTipo: {}.\n'.format(self.color, self.ruedas, self.tipo)



class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return 'Objeto de la clase: Motocicleta.\nColor: {}.\nRuedas: {}.\nTipo: {}:\nVelocidad : {} Km/h.\nCilindrada: {} cc. \n'.format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada)

#   Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehículos.


coche1 = Coche('Azul', 4, 290, 2.0)
camioneta1 = Camioneta('Gris', 6, 300, 2.5, 3000)
bicicleta1 = Bicicleta('Negro', 2, 'urbana')
motocicleta1 = Motocicleta('Rojo', 2, 'deportiva', 190, 150)

#   Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.


def catalogar(vehiculos):
    for v in vehiculos:
        print(v)

vehiculo = [
    coche1,
    camioneta1,
    bicicleta1,
    motocicleta1
]

#catalogar(vehiculo)
#   Modifica la función catalogar() para que reciba un argumento optativo ruedas,
#       haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento.

def catalogar_filtro(vehiculos, ruedas=None):
    for v in vehiculos:
        if v.ruedas == ruedas:
            print(v)


catalogar_filtro(vehiculo,2)

#   También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas.

#   Ponla a prueba con 0, 2 y 4 ruedas como valor.
