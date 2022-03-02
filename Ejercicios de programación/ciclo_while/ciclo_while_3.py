#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
#Precondición:
#se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

frase=input("Frase: ").strip()
cantidad=0
len_p_mas_larga=0
while len(frase) != 0:
    cantidad=cantidad+1
    i=frase.find(" ")
    if i != -1:
        palabra=frase[0:i]
        while i < len(frase) and frase[i] == " ":
            i=i+1
        frase=frase[i:]
    else:
        palabra=frase
        frase=""
    if len(palabra) > len_p_mas_larga:
        len_p_mas_larga=len(palabra)
        p_mas_larga=palabra
if cantidad > 0:
    print("Palabra más larga:", p_mas_larga)
print("Cantidad de palabras:", cantidad)