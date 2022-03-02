#Dado un número entero positivo, mostrar su factorial. 
# El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.

numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)