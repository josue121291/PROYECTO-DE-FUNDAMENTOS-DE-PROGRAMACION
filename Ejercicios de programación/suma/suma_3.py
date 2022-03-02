#Calcular la suma de tres números, ademas incluir una condicion de igualdad.

def sumar_numeros(a, b, c):
    #calcula la suma de tres numeros. si los res numeros iguales, 
    #la suma se multiplica por 3.
    
    suma = a + b + c
    
    if a == b and a == c:
        suma *= 3
        
    return suma 
print(sumar_numeros(2, 2, 7))
print(sumar_numeros(2, 2, 2))
         