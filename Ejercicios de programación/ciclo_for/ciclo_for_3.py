
#Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
#Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.


sumaPositivos=0
cantidadPositivos=0
sumaNegativos=0
for i in range(6):
   nro=int(input("Número: "))
   if nro>0:
       sumaPositivos=sumaPositivos+nro
       cantidadPositivos=cantidadPositivos+1
   else:
       sumaNegativos=sumaNegativos+nro
print("Sumatoria de los negativos: ", sumaNegativos)
if cantidadPositivos!=0:
   print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
else:
   print("No se ingresaron números positivos")