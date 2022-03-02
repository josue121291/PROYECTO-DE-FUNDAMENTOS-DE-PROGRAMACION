#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
#Finalmente, mostrar la sumatoria de todos los números ingresados.

total=0
nro=int(input("Número: "))
while nro != 0:
    total+=nro
    nro=int(input("Número: "))