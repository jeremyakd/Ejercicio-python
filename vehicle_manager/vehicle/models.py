from django.db import models

# Create your models here.
class Vehicle(models.Model):
    color = models.CharField(max_length=60)
    ruedas = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        abstract = True


class Coche(Vehicle):

    velocidad = models.IntegerField()
    cilindrada = models.IntegerField()

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return 'Coche'
        #return 'Objeto de la clase: Coche. \nColor: {}.\nRuedas: {}.\nVelocidad : {} Km/h \nCilindrada: {} cc.\n'.format(self.color, self.ruedas, self.velocidad, self.cilindrada)


class Camioneta(Vehicle):

    velocidad = models.IntegerField()
    cilindrada = models.IntegerField()
    carga = models.IntegerField()

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return 'Camioneta'
        #return 'Objeto de la clase: Camioneta. \nColor: {}.\nRuedas: {}.\nVelocidad : {} Km/h \nCilindrada: {} \nCarga: {} Kg.\n'.format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)

tipos = models.TextChoices('Urbana', 'Deportiva')


class Bicicleta(Vehicle):

    tipo = models.CharField(choices=tipos.choices, max_length=9)

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return 'Bicicleta'
        #return 'Objeto de la clase: Bicicleta. \nColor: {}.\nRuedas: {}.\nTipo: {}.\n'.format(self.color, self.ruedas, self.tipo)



class Motocicleta(Vehicle):

    tipo = models.CharField(choices=tipos.choices, max_length=9)
    velocidad = models.IntegerField()
    cilindrada = models.IntegerField()

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return 'Motocicleta'
        #return 'Objeto de la clase: Motocicleta.\nColor: {}.\nRuedas: {}.\nTipo: {}:\nVelocidad : {} Km/h.\nCilindrada: {} cc. \n'.format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada)
