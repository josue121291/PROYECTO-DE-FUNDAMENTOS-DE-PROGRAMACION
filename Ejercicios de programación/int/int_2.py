#Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.

numero1=int(input("Un número:"))
numero2=int(input("Otro número distinto:"))
if numero1>numero2:
    print(numero1, "es mayor")
else:
    print(numero2, "es mayor")