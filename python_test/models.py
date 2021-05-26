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
        return 'Coche'
        #return 'Objeto de la clase: Coche. \nColor: {}.\nRuedas: {}.\nVelocidad : {} Km/h \nCilindrada: {} cc.\n'.format(self.color, self.ruedas, self.velocidad, self.cilindrada)


class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return 'Ccamioneta'
        #return 'Objeto de la clase: Camioneta. \nColor: {}.\nRuedas: {}.\nVelocidad : {} Km/h \nCilindrada: {} \nCarga: {} Kg.\n'.format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)


class Bicicleta(Vehicle):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return 'Bicicleta'
        #return 'Objeto de la clase: Bicicleta. \nColor: {}.\nRuedas: {}.\nTipo: {}.\n'.format(self.color, self.ruedas, self.tipo)



class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return 'Motocicleta'
        #return 'Objeto de la clase: Motocicleta.\nColor: {}.\nRuedas: {}.\nTipo: {}:\nVelocidad : {} Km/h.\nCilindrada: {} cc. \n'.format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada)
