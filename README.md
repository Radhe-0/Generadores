# Generadores de datos para practicar modelado de machine learning

Esta es una librería que les permitirá generar datos de manera aleatoria con Python. Con ella podrán tener datos para entrenar un modelo de inteligencia artificial con una pequeña línea de código sin tener que buscar datasets.

# Setup

Para instalar esta librería lo único que tienen que hacer es forkear este repositorio y luego clonarlo en su sistema.

### Requisitos:
-   Numpy
-   Pandas

# Cómo usar

Para tener disponibles todas las funciones de esta librería, es necesario crear un nuevo archivo de python dentro de la carpeta donde se encuentra el archivo `Generadores.py` e importarla con la siguiente línea de código:

    from Generadores import *

Con esto ya tendrán disponibles las siguientes funciones:

```python
DatosLineales()
DatosNoLineales()
DatosClusters()
DatosLRegression()
DatosSVM()
```
### Ejemplos:

La mejor manera de usar esta librería es llamar a una función y guardarla en una variable:

```python
datos = DatosClusters()
print(datos)
```

output:

```
[(45.27023440496043, 35.27023440496043),
 (6.032939073068473, 91.03293907306848),
 (86.20274324543908, 54.20274324543908),
 (99.22888144766773, 19.228881447667735),
 (21.61789445804867, 99.61789445804867),
 (38.97369973778412, 8.973699737784122),
 (7.150489902687079, 29.15048990268708),
 (16.693213712990573, 34.69321371299057),
 (4.872569662723574, 96.87256966272358),
 (68.81106612969232, 28.81106612969233)]
```
### Más ejemplos:

```python
datos = DatosLineales()
df = pd.DataFrame(datos, columns = ['x', 'y'])
df.plot.scatter(x = 'x', y = 'y')
```
output:

<img src="https://i.imgur.com/53Mlly7.png"/>

```python
datos = DatosNoLineales(80)
data_frame = pd.DataFrame(datos, columns=['x', 'y'])
data_frame.plot.scatter(x='x', y='y')
```

output:

<img src="https://i.imgur.com/iDfPV3l.png"/>
