# Generadores de datos para practicar modelado de machine learning

Este módulo les permitirá generar datos de manera aleatoria con Python. Con ellos tendrán la capacidad de entrenar un modelo de inteligencia artificial con una pequeña línea de código sin tener que buscar datasets.

# Setup

Para instalar este módulo lo único que tienen que hacer es forkear este repositorio y luego clonarlo en su sistema.

### Requisitos:
-   Numpy
-   Pandas

# Cómo usar

Para tener disponibles todas las funciones de este módulo, es necesario crear un nuevo archivo de python dentro de la carpeta donde se encuentra el archivo `Generadores.py` e importarla con la siguiente línea de código:

```python
from Generadores import *
```

Con esto ya tendrán disponibles las siguientes funciones:

```python
DatosLineales()
DatosNoLineales()
DatosClusters()
DatosLRegression()
DatosSVM()
DatosDistNormal()
DatosDistNormal3D()
```
### Ejemplo:

La mejor manera de usar este módulo es llamar a una función y guardarla en una variable:

```python
datos = DatosClusters()
print(datos)
```

>output:

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
datos = DatosLineales(100)
df = pd.DataFrame(datos, columns = ['x', 'y'])
df.plot.scatter(x = 'x', y = 'y')
```
>output:

<img src="https://i.imgur.com/53Mlly7.png"/>



```python
datos = DatosNoLineales(80)
df = pd.DataFrame(datos, columns=['x', 'y'])
df.plot.scatter(x='x', y='y')
```

>output:

<img src="https://i.imgur.com/iDfPV3l.png"/>



```python
datos = DatosLRegression(20)
data_frame = pd.DataFrame(datos, columns=['eje x', 'eje y'])
data_frame.plot.scatter(x='eje x', y='eje y')
```

>output:

<img src="https://i.imgur.com/PzOCsup.png"/>



```python
datos = DatosSVM(40)
df = pd.DataFrame(datos, columns=['x', 'y'])
df.plot.scatter(x='x', y='y')
```
>output:

<img src="https://i.imgur.com/GNiMeew.png"/>


```python
datos = DatosClusters(150)
df = pd.DataFrame(datos, columns=['x', 'y'])
df.plot.scatter(x='x', y='y')
```

>output:

<img src="https://i.imgur.com/Z4X8TUF.png"/>



# Aplicaciones al modelado de machine learning

```python
# Para KMeans Clustering

# Importamos las librerías (también usaremos numpy y pandas)
from sklearn.cluster import KMeans
import seaborn as sns

# Cargamos los datos
datos = DatosClusters(200)
df = pd.DataFrame(datos, columns=['x', 'y'])

# Transformamos los datos en un array de numpy (dos formas)
# NOTA: Son arrays 2D de (150, 2)
datos_transformados = df.to_numpy() # Primera forma: A través de un dataframe
datos_transformados = np.asarray(datos) # Segunda forma: A través de una lista

# Modelamos
modelo = KMeans(n_clusters=5) # Creamos el modelo
modelo.fit(datos_transformados) # Entrenamos el modelo
predicciones = modelo.predict(datos_transformados) # Hacemos las predicciones

# Graficamos
sns.scatterplot(x='x', y='y', data=df, hue=predicciones, palette='Set1')
```
>output:

<img src="https://i.imgur.com/ECPAl4G.png"/>



>Más ejemplos en `Generador_de_datos.ipynb`
