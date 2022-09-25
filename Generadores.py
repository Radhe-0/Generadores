import numpy as np
import pandas as pd


############
def DatosLineales(num=10):

    x = 2 * np.random.rand(num,1)
    x_ = [float(i) for i in x]
    y = np.random.randint(1,10) + np.random.randint(4,10) * x + np.random.randn(num,1)
    y_ = [float(i) for i in y]
    lista = []

    for i in zip(x_,y_):
        lista.append(i)

    return lista


#############
def DatosNoLineales(num=10):

    x = 2 * np.random.rand(num,1)
    x_ = [float(i) for i in x]
    y = x + 2 * x ** 3 + np.random.randn(num,1)
    y_ = [float(i) for i in y]
    lista = []

    for i in zip(x_,y_):
        lista.append(i)

    return lista


###########
def DatosClusters(num=10):

    numeros = np.random.rand(num)
    int_x = np.random.randint(0,100,size=num)
    int_y = np.random.randint(0,100,size=num)
    eje_x = np.sum([int_x, numeros], axis=0)
    eje_y = np.sum([int_y, numeros], axis=0)
    puntos = []

    for i in zip(eje_x, eje_y):
        puntos.append(i)

    return puntos


###########
def DatosLRegression(num=10):

    ceros = np.zeros(num)
    random_1 = np.random.rand(num)
    random_2 = np.random.randint(1,6,size=(1,num))
    valores = random_2 + random_1
    lista = []

    for i in zip(valores[0], ceros):
        lista.append(i)

    unos = np.ones(num)
    random_3 = np.random.rand(num)
    random_4 = np.random.randint(6,11,size=(1,num))
    valores_2 = random_4 + random_3

    for i in zip(valores_2[0], unos):
        lista.append(i)

    return lista


###########
def DatosSVM(num=10):

    X = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    Y = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    lista = []

    for i in zip(X,Y):
        lista.append(i)

    return lista
###########
def DatosSVM3D(num=10):

    X = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    Y = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    Z = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    lista = []

    for i in zip(X,Y,Z):
        lista.append(i)

    return lista
###########
def DatosDistNormal(num=10):

    y = np.random.normal(50,0.03,num)

    x = np.linspace(0,1,num)
    lista = []

    for i in zip(x,y):
        lista.append(i)

    return lista
###########
def DatosDistNormal3D(num=10):

    y = np.random.normal(50,0.16,num)
    x = np.linspace(0,1,num)
    z = np.random.normal(1000,0.13,num)
    lista = []

    for i in zip(x,y,z):
        lista.append(i)

    return lista
