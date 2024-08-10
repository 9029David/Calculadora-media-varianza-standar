import numpy as np

def arreglo_media (arr):
    axis1 = list(arr.mean(axis=0))
    axis2 = list(arr.mean(axis=1))
    flattened = arr.mean()
    media = [axis1, axis2, flattened]
    return media

def arreglo_varianza (arr):
    axis1 = list(arr.var(axis=0))
    axis2 = list(arr.var(axis=1))
    flattened = arr.var()
    varianza = [axis1, axis2, flattened]
    return varianza
    
def arreglo_desviacion (arr):
    axis1 = list(arr.std(axis=0))
    axis2 = list(arr.std(axis=1))
    flattened = arr.std()
    desviacion = [axis1, axis2, flattened]
    return desviacion

def arreglo_max (arr):
    axis1 = list(arr.max(axis=0))
    axis2 = list(arr.max(axis=1))
    flattened = arr.max()
    maximo = [axis1, axis2, flattened]
    return maximo

def arreglo_min (arr):
    axis1 = list(arr.min(axis=0))
    axis2 = list(arr.min(axis=1))
    flattened = arr.min()
    minimo = [axis1, axis2, flattened]
    return minimo

def arreglo_sum (arr):
    axis1 = list(arr.sum(axis=0))
    axis2 = list(arr.sum(axis=1))
    flattened = arr.sum()
    suma = [axis1, axis2, flattened]
    return suma

def formato_diccionario (arr):
    resultado = {}
    resultado['mean'] = arreglo_media(arr)
    resultado['variance'] = arreglo_varianza(arr)
    resultado['standard deviation'] = arreglo_desviacion(arr)
    resultado['max'] = arreglo_max(arr)
    resultado['min'] = arreglo_min(arr)
    resultado['sum'] = arreglo_sum(arr)
    return resultado

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(lista).reshape(3, 3)
    calculations = formato_diccionario(arr)
    return calculations