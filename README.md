# Ejercicio-python
Examen desarrollo ISBA - Java &amp; Python

## Ejercicio 1 => test-iterator

- Dé un ejemplo de una situación que requiera el uso de ThreadLocal.

    Podemos usar esta clase para evitar incluir en cada método el parámetro de ese dato si es usado en multitud de métodos simplificando en gran medida el código. En las aplicaciones web este dato puede ser el usuario que se ha autenticado, el dominio por el que se ha accedido a la aplicación, el dispositivo móvil, el idioma del usuario o cualquier otra información que queramos esté disponible de forma global en el hilo de ejecución.


- ¿Cuándo es necesario marcar una variable como volatile?

    Sirve para marcar una variable que es compartida por varios hilos, indicando que le valor de esta variable puede cambiar en cualquier momento y debe ser visible por todos los hilos que la usen.

- ¿Qué lleva a una situación de deadlock? ¿Cómo puede resolverse?

    - Se da cuando dos o mas hilos, se bloquean mutuamente esperandose el uno al otro. Luego de analizar el funcionamiento y detectar el problema, se puede optar por reordenar la logica y el acceso a los recursos compartidos.
<hr>

## Sean los siguientes esquemas relacionales:

Vuelo(VueloNro, Desde, Hacia, Distancia, Partida, Arribo, Precio)
Aeronave(AId, ANombre, Rango)
Certificado(EId, AId)
Empleado(EId, Enombre, Sueldo)

![flujo_duenias2](vehicle_manager/UML_DER.png)

La relación Empleado contiene datos de todos los empleados de la compañía, entre ellos los pilotos.
En la relación Certificado solo figuran los pilotos certificados para volar una determinada aeronave.

Responder la siguiente consulta en SQL:

“Listar los nombres de los pilotos que pueden volar 
aeronaves con rango de crucero mayor a 5000 millas 
pero que solo está certificado con aviones Boeing”

SELECT Enombre AS 'Nombre' 
FROM Empleados E 
JOIN Certificado C 
ON E.EId = C.EId
JOIN Aeronave A 
ON A.AId = C.AId 
WHERE A.Rango > 5000 
AND A.ANombre LIKE '%Boeing%'
<hr>


## Python => python_test
<hr>
## Yapa vehicle_manager
Es el ejercicio de python con Django.

        virtualenv entorno-prueba --python=python3
        source entorno-prueba/bin/activate
        cd vehicle_manager
        pip install -r requirementrs.txt
        python manage.py runserver

<hr>

## Web services

### Manejo de performance en alta demanda

### Solución vía infraestructura
- Se ha de diagnosticar el punto donde la performance comienza a descender y que servicio es el primero en ser afectado.
Evaluando la herramienta de orquestación (ya sea por VM o containers) se configurará un trigger para balancear la carga, escalando (idealmente) de manera horizontal.
### Solución vía funcionalidad
- En caso de no poder resolver por infraestructura y asumiendo que el código es performante evaluaría poder administrar la respuesta al cliente de manera desatendida tomamos el ejemplo de que la confirmación de la compra se ve demorada en la integración de los postnet virtuales, cuando hay llamadas concurrentes
    - Al finalizar la compra el usuario no sabe si ha sido exitosa, de manera tal que le mostraremos un mensaje para confirmarle que la solicitud de compra ha sido recibida y que recibirá el resultado final dentro de las pŕoximos minutos


### Ver reportes de ventas en tiempo real
- Emplearía un stack de tecnologías ETL, que están pensadas para reportes en tiempo real como Elasticsearch, donde podemos implementar lo siguiente:

- Con Filebeat hacemos la extracción de los logs de los servicios por ejemplo un proceso de funel:
    - Usuario arriba en la plataforma
    - Selecciona el espectáculo de interés
    - Solicitud recibida
    - Solicitud procesada con estado (confirmado/ rechazado)
    - Usuario notificado
- Con Logtash realizamos la transformación de los logs a, por ejemplo json, para normalizar los documentos para poder explotarlos en el dashboard de Kibana
- Con Kibana haremos la explotación de los datos usando, por ejemplo, el gráfico de barras para las ventas realizadas (eje vertical) durante el periodo que seleccione el usuario (horas, días, meses).

### Reporte mensual de ventas

Utilizando la solución del punto anterior es necesario observar que:
Se duplica la información
Ya no se bloquearía la main DB del sistema al momento de consultar el reporte mensual.
