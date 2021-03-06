# PROYECTO-DE-FUNDAMENTOS-DE-PROGRAMACION

# ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente par el desarrollo web y de aplicaciones informáticas. 

# ¿Qué es una variable?

En algunos lenguajes de programación, las variables se pueden entender como "cajas" en las que se guardan los datos, pero en python las varriables son "etiquetas" que permiten hacer referenci a los datos 

Ejemplo:

```python
a = 2
```

## Nombrando una variable

Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o numeros al principio. 

Ejemplo:

* Válido 

```python
_variable = 10

 vari_able = 20

 variable10 = 30

 variable = 60

 variaBle = 10
 ```

* No válido


```python
2variable = 10

var-iable = 10

var iable = 10
```

## Asignando valores a una variable

Para asignar un valor (un dato) a una variable se utiliza el operador de asignación ``=``.
En la operacion de asignación se ven incolucradas tres parte:

* El operador de asignación ``=``

* Un identificador o nombre de variable, a la izquierda del operador.

* Un literal, una expresión, una llamada a una función o una combinacion de todos ellos.


## Operadores básicos

Los operadores aritméticos se utilizan prara realizar operaciones matemáticas como la suma ``+``, resta``-``, multiplicación``*`` divición``/`` y el módulo``%``.

Ejemplos:
``` python
suma = +
resta = -
multiplicación = *
división = /
módulo = %
```

### Suma

En python, ``+`` es el operador de suma. se utiliza para sumar 2 o más valores.

Ejemplo:

```python
valor1 = 2

valor2 = 3
```
- usando el operador de adición

```python
resul =  valor1 + valor2

  print:("resultado")
```
 salida: 

    5

### Resta

En python, ``-`` es el operador de sustracción. Se utiliza para restar el segundo del primer valor.

 Ejemplo:
 
 ```python
 valor1 = 2
 
 valor2 = 3
  
 resul = valor1 - valor2
 ```
    print("resultado")
 
  salida: 
 
    -1
  

### Multiplicación
En python, ``*`` es el operador de multiplicación. Se utiliza para encontrar el producto de 2 valores.

Ejemplo:

```python
valor1 = 2

valor2 = 3

resul = valor1 * valor2

  print:("resultado")
```
  
  salida:

    6

### División

En python, ``/`` es el operador de divición. se utiliza para encontrar el cociente cuando el primer operador se divide por el segundo.

Ejemplo:

```python
valor1 = 3

valor2 = 2

resul = valor1 / valor2

  print:("resultado")
```
  salida: 

    1.5
  

### Módulo

En python, ``%`` es el operador de módulo. Se utiliza para encontrar el resto cuando el primer operador se divide por el segundo.

Ejemplo:

```python
valor1 = 3

valor2 = 2

resul = valor1 % valor2

  print:("resultado")
  ```

  salida:
  
    1
 

# Tipos de datos en Python

Los tipos de datos básicos en Python son los siguientes:

## Integer

Este tipo de de datos se corresponde con números enteros, es decir, sin parte decinmal.

Ejemplo:

```python
x = 9

y = 64521

z = -254


    *esto te permite sumar dos variables directamente.
    
    print(y + z)
  ```

## Float

Este tipo de dato corresponde con números reales con partes parte decimal. Cabe destacar que el separador decimal en Python es el punto ``.``y no la coma``,``.

Ejemplo:

 ```python
 x = 1.10
 
 y = 2.50
 
 z = -65.41
   
    print(x)
    print(x - z)
  ```
   
## String

Este tipo de datos corresponde con una cadena de caracteres.

Ejemplo:

```python
cadena = "programa de python"

type(cadena)

<class "str">

    print("cadena")
 ```   

# Casting en Python

Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.

```python
a = 1   # <class 'int'>  
b = 2.3 # <class 'float'>  
a = a + b  
print(a)       # 3.3  
print(type(a)) # <class 'float'>
```

Existen dos:
Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciónes con dos tipos distintos.

## List

Se trata de conjuntos ordenados de elementos, encerrados por corchetes y separdos por comas. el orden comienza con el índice 0 para el primer ligar d ela lista. pueden agruparse valores de distintos tipos de datos básicos, y es posible agregar, eliminar o modificar elemtos de las listas  en cualquier momento ( decimos que las listas son mutables en Python)

Ejemplo1:

```python
lista1 = ["cuaderno", "lápiz", "libro"]
 
    print:("lista1")
 ```
salida
  
    cuaderno
    lápiz
    libro
 
Ejemplo2:
 
 ```python
 lista2 = ["manzana", "uva", "pera"]
 
    print:("lista2")
 ``` 
 salida
 
    manzana
    uva
    pera
  
Ejemplo3:

 ```python
 lista3 = [1, 5, 7, 9, 3]
 
    print:("lista3")
```
salida

    1
    5
    7
    9
    3

## Tuple

El tuple o las tuplas son básicamente listas de elementos estática, es decir, que no pueden modificarse (decimos que el tuple es inmutable en Python). para su definicion en lugar de ``[]`` se encierran valores separdos por comas entre paréntesis ``(, , ,)``.

Ejemplo1:

```python
mi_tuple1 = (1, 2, 3)

    print:("mi_tuple1)
```
salida
   
    1
    2
    3
    
Ejemplo2:

```python
mi_tuple2 = (1, "Hello", 3.4)``

    print:("mi_tuple2)
```
salida

    1
    Hello
    3
    4
    
Ejemplo3:

```python
mi_tuple3 = ("mouse", [8, 4, 6], (1, 2, 3))

    print:("mi_tuple3)
```    
salida

    mouse
    8
    4
    6
    1
    2
    3

## Dictionary

En los diccionarios cada elemento se compone de un par clave-valor, y para su definición es necesario encerrar los elementos entre llaves. Es posible acceder a un valor utilizando su clave, pero no al revés. Por este motivo, no se pueden repetir las claves para elementos distintos, pero sí es posible agregar, eliminar o modificar valores (Los diccionarios son mutables).

Ejemplo:

```python
my_diccionario1 = {'nombre': 'Jack', 'edad': 26}

    print(mi_diccionario1['nombre'])
    
    print(mi_diccionario.get('edad'))
    
    print(mi_diccionario.get('dirección'))
    
    print(mi_diccionario['dirreción'])
```
salida

    Jack
    26
    None
    Traceback (most recent call last):
    File "<string>", line 15, in <module>
    print(my_dict['address'])
    KeyError: 'address'
      
      
# Tomando decisiones

## Sentencia if

La estructura de control ``if``.... permite que un programa ejecute unas instrucciones cuando se cumplan una condición. En inglés ``if`` significa ``si``

 La sintaxis de la sentencia condicional ``if``.... es la siguiente.
 
 `` if  condición :
        "aquí van las órdenes que se ejecutan si la condicion es cierta
        y que pueden ocupar varias lineas".
        ``
- La condición se evalua siempre.
  * Si el resultado es ``True`` se ejecuta el bloque de sentencias.
  * Si el resultado es ``False`` no se ejecuta el bloque de sentencias.

La primera línea contiene la condición a evaluar y es una expresión lógica. Esta línea debe terminar siempre por dos puntos ``(:)``.

Ejemplo de ``if``:

```python
numero = int(input("escriba un nuemro positivo:"))

if numero < 0:

    print("¡Le he dicho que escriba un número positivo!)
     
    print(f"Ha escrito el numero {numero}")
```
salida:

    escriba un número positivo: -5

    ¡Le he dicho que escriba un número positivo!

    Ha escrito el numero -5 


## Sentencia if... else....

La estructura de control ``if``.... ``else``... permite que un programa ejecute unas instrucciones cuando se cumple una condición y otras instrucciones cuando no se cumple esa condición. En inglés ``if`` significa ``si`` (condición) y ``else`` significa ``si no``. La orden en python se escribe asi:

La sintaxis de la construccion ``if``... ``else``... es la siguiente:

```python
if condición:

    "aquí van las órdenes que se ejecutan si la condición es cierta y que pueden ocupar varias líneas"
   
 else:
 
     "y aqui van las que se ejecutan si la condicion es falsa y que tambien puedenocupar varias líneas."
 ```
     
La ejecución de esta construcción es la siguiente:

- La condición se evalúa siempre.
* Si el resultado es ``True`` se ejecuta solamente el bloque de sentencia 1.
* Si el resultado es ``False`` se ejecuta solamente el bloque de sentencia 2.

La primera línea contiene la condición a evaluar. Esta línea debe terminar siempre por dos puntos ``(:)``.

Ejemplo:

```python
edad = int(input("¿Cuántos años tienes?"))

if edad < 18:

    print("Es usted menor de edad")
    
else:

     print("Es usted mayor de edad")

    print("¡Hasta la próxima!")
```
salida

    ¿Cuántos años tiene? 17

    Es usted menor de edad

    ¡Hasta pronto!


## Ciclo For

Los ciclos for son lo que se conoce como estructuras de control de flujo cíclicas o simplemente estructuras cíclicas, estos ciclos, como su nombre lo sugiere, nos permiten ejecutar una o varias líneas de código de forma iterativa, conociendo un valor especifico inicial y otro valor final, además nos permiten determinar el tamaño del paso entre cada "giro" o iteración del ciclo.

Su sintaxis es la siguiente:

```python
for <elem> in <iterable>:
   
   <tu codigo>
```
   
Aquí, ``elem`` es la variable que toma el valor del elemento dentro del iterador en cada paso del bucle. Este finaliza su ejecución cuando se recorren todos los elementos.

Ejemplo:

```python
nums = [4, 78, 9, 84]

for n in nums:

    print(n)
```
salida

    4
    78
    9
    84

## Ciclo While

Un bucle ``wile`` permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor ``True``).
La sintaxis del bucle``while`` es la siguiente:

```python
while condición:

    cuerpo del bucle
 ```   
 La ejecución de esta estructura de control ``while`` es la siguiente:
 
 - Python evalúa la condición:
 * si el resultado es ``True``, se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.
 * si el resultado es ``False``, el cuerpo del bucle no se ejecuta y continúa la ejecución del resto del programa.

La variable o las variables que aparezcan en la condición se suelen llamar variables de control. Las variables de control deben definirse antes del bucle ``while`` y modificarse en el bucle ``while``.

Ejemplo:

```python
i = 3
  while i <= 3:
  
    print(i)
    i += 1
    print("programa terminado")
```
   
salida

    1
    2
    3
    programa terminado
   
## Break 

En Python, la instrucción``break`` le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción ``break`` dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción ``if`` condicional.

Ejemplo:

```python
numero=0

for numero in range(10):
     
     if numero = 5
      break
      print("numero es" + str(numero))
      print("out of loop")
```    
salida 
 
    numero es 0
    numero es 1
    numero es 2
    numero es 3
    numero es 4
    out of loop 

## Continue

La instrucción, ``continue`` da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.

La instrucción, ``continue`` se encuentra dentro del bloque de código abajo de la instrucción del bucle, generalmente después de una instrucción if condicional.

Ejemplo:

```python
numero = 0

for numero in range(10):

    if numero = 5
      continue
       print("numero es" + str(numero))
       print("out of loop")
```
 salida
 
    numero es 0
    numero es 1
    numero es 2
    numero es 3
    numero es 4 
    numero es 6
    numero es 7
    numero es 8
    numero es 9
    out of loop
    
