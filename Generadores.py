import numpy as np
import pandas as pd

#################################################

def DatosLineales(num=10):

    x = 2 * np.random.rand(num,1)
    x_ = [float(i) for i in x]
    y = np.random.randint(1,10) + np.random.randint(4,10) * x + np.random.randn(num,1)
    y_ = [float(i) for i in y]
    lista = []

    for i in zip(x_,y_):
        lista.append(i)

    return lista

#################################################

def DatosLineales3D(num=10):

    x = 2 * np.random.rand(num,1)
    x_ = [float(i) for i in x]
    y = np.random.randint(1,10) + np.random.randint(4,10) * x + np.random.randn(num,1)
    y_ = [float(i) for i in y]
    lista = []

    for i in zip(x_,y_):
        lista.append(i)

    return lista

#################################################

def DatosNoLineales(num=10):

    x = 2 * np.random.rand(num,1)
    x_ = [float(i) for i in x]
    y = x + 2 * x ** 3 + np.random.randn(num,1)
    y_ = [float(i) for i in y]
    lista = []

    for i in zip(x_,y_):
        lista.append(i)

    return lista

#################################################

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

#################################################

def DatosClusters3D(num=10):

    numeros = np.random.rand(num)
    int_x = np.random.randint(0,100,size=num)
    int_y = np.random.randint(0,100,size=num)
    int_z = np.random.randint(0,100,size=num)
    eje_x = np.sum([int_x, numeros], axis=0)
    eje_y = np.sum([int_y, numeros], axis=0)
    eje_z = np.sum([int_z, numeros], axis=0)

    lista = []

    for i in zip(eje_x, eje_y, eje_z):
        lista.append(i)
    
    return lista

#################################################

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

#################################################

def DatosSVM(num=10):

    X = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    Y = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    lista = []

    for i in zip(X,Y):
        lista.append(i)

    return lista

#################################################

def DatosSVM3D(num=10):

    X = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    Y = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    Z = (np.r_[np.random.randn(num, 2) - [2, 2], np.random.randn(num, 2) + [2, 2]]).reshape(-1)
    lista = []

    for i in zip(X,Y,Z):
        lista.append(i)

    return lista

#################################################

def DatosSVM2(num=10):

    X = np.linspace(0,100,num)
    Y = np.linspace(0,100,num)

    Xmod = X * np.random.randn(num)
    Ymod = Y * np.random.randn(num)

    Xmod2 = X * np.random.randn(num) + 500
    Ymod2 = Y * np.random.randn(num) + 500

    Xmod3 = X * np.random.randn(num)
    Ymod3 = Y * np.random.randn(num) + 500

    Xmod4 = X * np.random.randn(num) + 500
    Ymod4 = Y * np.random.randn(num)

    lista = []
    
    for i in zip(Xmod, Ymod):
        lista.append(i)

    for i in zip(Xmod2, Ymod2):
        lista.append(i)

    for i in zip(Xmod3, Ymod3):
        lista.append(i)

    for i in zip(Xmod4, Ymod4):
        lista.append(i)

    return lista
#################################################

def DatosSVM23D():
    
    lista = []
    
    X = np.linspace(0,100,num)
    Y = np.linspace(0,100,num)
    Z = np.linspace(0,100,num)

    Xmod = X * np.random.randn(num)
    Ymod = Y * np.random.randn(num) + 700
    Zmod = Z * np.random.randn(num)


    Xmod2 = X * np.random.randn(num) + 500
    Ymod2 = Y * np.random.randn(num) + 700
    Zmod2 = Z * np.random.randn(num)

    Xmod3 = X * np.random.randn(num)
    Ymod3 = Y * np.random.randn(num) + 700
    Zmod3 = Z * np.random.randn(num) + 500

    Xmod4 = X * np.random.randn(num) + 500
    Ymod4 = Y * np.random.randn(num) + 700
    Zmod4 = Z * np.random.randn(num) + 500


    for i in zip(Xmod, Ymod, Zmod):
        lista.append(i)

    for i in zip(Xmod2, Ymod2, Zmod2):
        lista.append(i)

    for i in zip(Xmod3, Ymod3, Zmod3):
        lista.append(i)

    for i in zip(Xmod4, Ymod4, Zmod4):
        lista.append(i)

    X = np.linspace(0,100,num)
    Y = np.linspace(0,100,num)
    Z = np.linspace(0,100,num)

    Xmod5 = X * np.random.randn(num) - 500
    Ymod5 = Y * np.random.randn(num)
    Zmod5 = Z * np.random.randn(num) - 500


    Xmod6 = X * np.random.randn(num)
    Ymod6 = Y * np.random.randn(num)
    Zmod6 = Z * np.random.randn(num) - 500

    Xmod7 = X * np.random.randn(num) - 500
    Ymod7 = Y * np.random.randn(num)
    Zmod7 = Z * np.random.randn(num)

    Xmod8 = X * np.random.randn(num)
    Ymod8 = Y * np.random.randn(num)
    Zmod8 = Z * np.random.randn(num)

    for i in zip(Xmod5, Ymod5, Zmod5):
        lista.append(i)

    for i in zip(Xmod6, Ymod6, Zmod6):
        lista.append(i)

    for i in zip(Xmod7, Ymod7, Zmod7):
        lista.append(i)

    for i in zip(Xmod8, Ymod8, Zmod8):
        lista.append(i)

    return lista

#################################################

def DatosDistNormal(num=10):

    y = np.random.normal(50,0.03,num)

    x = np.linspace(0,1,num)
    lista = []

    for i in zip(x,y):
        lista.append(i)

    return lista

#################################################

def DatosDistNormal3D(num=10):

    y = np.random.normal(50,0.16,num)
    x = np.linspace(0,1,num)
    z = np.random.normal(1000,0.13,num)
    lista = []

    for i in zip(x,y,z):
        lista.append(i)

    return lista

#################################################

class generadores():
    pass

    def info(self):
        print('Funciones disponibles:')
        print('----------------------------------------------')
        print('DatosLineales()')
        print('DatosLineales3D()')
        print('DatosNoLineales()')
        print('DatosClusters()')
        print('DatosClusters3D()')
        print('DatosLRegression()')
        print('DatosSVM()')
        print('DatosSVM3D()')
        print('DatosSVM2()')
        print('DatosDistNormal')
        print('DatosDistNormal3D()')
        print('----------------------------------------------')
        print('Más info en: https://github.com/Radhe-0/Generadores')

generadores = generadores()
