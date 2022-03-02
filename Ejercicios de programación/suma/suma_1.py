#Escribí una función llamada esPar que reciba como parámetro un número y retorne True si el número es par ó False si es impar.
#Utilizar esta función en un programa que solicite al usuario el ingreso de 10 números y que luego muestre, por separado, la suma de todos los pares y la suma de todos los impares.

def esPar(numero):
    return numero%2 == 0

sumaPares=0
sumaImpares=0
for i in range(10):
    num=int(input("Número:"))
    if esPar(num):
        sumaPares=sumaPares+1
    else:
        sumaImpares=sumaImpares+1
print("Suma de los pares:", sumaPares)
print("Suma de los impares:", sumaImpares)