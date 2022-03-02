#Escribí un programa que, dado un número entero, muestre su valor absoluto. 
#Recordá que, para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), 
#mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 
#(el valor absoluto de -52 es 52).

numero=int(input("Número:"))
if numero<0:
    numero=numero*-1
print("Valor absoluto:", numero)