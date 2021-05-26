from models import Coche, Camioneta, Bicicleta, Motocicleta

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
#   También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas.
#   Ponla a prueba con 0, 2 y 4 ruedas como valor.


def catalogar_filtro(vehiculos, ruedas=None):
    if ruedas:
        vehiculos = list(filter(lambda x: x.ruedas == ruedas, vehiculos))
        if vehiculos == []:
            print('{} \n*  Lo sentimos, no hay resultados para su busqueda. Prueba de nuevo.  *\n{}\n'.format('* '*36, '* '*36))
        else:
            print('{}\n*  Se han encontrado {} vehículos con {} ruedas:  *\n{}\n'.format('* '*25, len(vehiculos), ruedas, '* '*25))
    #print("fiter_vehicles", fiter_vehicles)
    for v in vehiculos:
        if not ruedas or ruedas==v.ruedas:
            print('Objeto de tipo {}.'.format(v))
            for (key, value) in v.__dict__.items():
                print('{}: {}.'.format(key, value))
            print('-'*30)

while True:
    pepe = input()
    if not pepe:
        catalogar_filtro(vehiculo)
    elif int(pepe) == 0:
        break
    else:
        catalogar_filtro(vehiculo, int(pepe))