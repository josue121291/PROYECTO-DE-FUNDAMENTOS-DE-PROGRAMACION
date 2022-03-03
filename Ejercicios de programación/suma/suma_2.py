#Sumar dos números. si la suma esta entre 10 y 30, retornar 30.

from tkinter import Y


def sumar (x, y):
    
    '''
    Suma dos números. Si la suma está entre 10 y 30, retorna 30.
    '''
    suma = x + y
    
    if suma in range(10, 30 + 1):
        return 30
    else:
        return suma
    
print(sumar(7,3))
print(sumar(7,23))
print(sumar(12,17))
print(sumar(23,17))