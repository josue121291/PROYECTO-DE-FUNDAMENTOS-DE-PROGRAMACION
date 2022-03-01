# PROYECTO-DE-FUNDAMENTOS-DE-PROGRAMACION

# ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente par el desarrollo web y de aplicaciones informáticas. 

# ¿Qué es una variable?

En algunos lenguajes de programación, las variables se pueden entender como "cajas" en las que se guardan los datos, pero en python las varriables son "etiquetas" que permiten hacer referenci a los datos ejemplo:

`` 
a = 2
``

## Nombrando una variable

Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o numeros al principio. ejemplo:

* Válido 

``_variable = 10``

 ``vari_able = 20``

 ``variable10 = 30``

 ``variable = 60``

 ``variaBle = 10``

* No válido


``2variable = 10``

``var-iable = 10``

``var iable = 10``

## Asignando valores a una variable

Para asignar un valor (un dato) a una variable se utiliza el operador de asignación ``=``.
En la operacion de asignación se ven incolucradas tres parte:
* El operador de asignación ``=``
* Un identificador o nombre de variable, a la izquierda del operador.
* Un literal, una expresión, una llamada a una función o una combinacion de todos ellos.
Ejemplos:



## Operadores básicos

Los operadores aritméticos se utilizan prara realizar operaciones matemáticas como la suma ``+``, resta``-``, multiplicación``*`` divición``/`` y el módulo``%``.

### Suma

En python, ``+`` es el operador de suma. se utiliza para sumar 2 o más valores.
Ejemplo:

``valor1 = 2``

``valor2 = 3``

- usando el operador de adición

``resul =  valor1 + valor2``

  ``print:("resultado")``

 salida: 

    5

### Resta

En python, ``-`` es el operador de sustracción. Se utiliza para restar el segundo del primer valor.
 Ejemplo:
 
 ``valor1 = 2``
 
 ``valor2 = 3``
  
 ``resul = valor1 - valor2``
 
  ``print("resultado")``
 
  salida: 
 
    -1
  

### Multiplicación
En python, ``*`` es el operador de multiplicación. Se utiliza para encontrar el producto de 2 valores.
Ejemplo:

``valor1 = 2``

``valor2 = 3``

``resul = valor1 * valor2``

  ``print:("resultado")``
  
  salida:

    6

### División

En python, ``/`` es el operador de divición. se utiliza para encontrar el cociente cuando el primer operador se divide por el segundo.
Ejemplo:

``valor1 = 3``

``valor2 = 2``

``resul = valor1 / valor2``

  ``print:("resultado")``

  salida: 

    1.5
  

### Módulo

En python, ``%`` es el operador de módulo. Se utiliza para encontrar el resto cuando el primer operador se divide por el segundo.
Ejemplo:

``valor1 = 3``

``valor2 = 2``

``resul = valor1 % valor2``

  ``print:("resultado")``

  salida:
  
    1
 

# Tipos de datos en Python

Los tipos de datos básicos en Python son los siguientes:

## Integer

Este tipo de de datos se corresponde con números enteros, es decir, sin parte decinmal.
Ejemplo:

## Float

Este tipo de dato corresponde con números reales con partes parte decimal. Cabe destacar que el separador decimal en Python es el punto ``.``y no la coma``,``.
Ejemplo:


## String

Este tipo de datos corresponde con una cadena de caracteres.
Ejemplo:


# Casting en Python

## List

Se trata de conjuntos ordenados de elementos, encerrados por corchetes y separdos por comas. el orden comienza con el índice 0 para el primer ligar d ela lista. pueden agruparse valores de distintos tipos de datos básicos, y es posible agregar, eliminar o modificar elemtos de las listas  en cualquier momento ( decimos que las listas son mutables en Python)

## Tuple

El tuple o las tuplas son básicamente listas de elementos estática, es decir, que no pueden modificarse (decimos que el tuple es inmutable en Python). para su definicion en lugar de ``[]`` se encierran valores separdos por comas entre paréntesis ``(, , ,)``.
Ejemplo:


## Dictionary

En los diccionarios cada elemento se compone de un par clave-valor, y para su definición es necesario encerrar los elementos entre llaves. Es posible acceder a un valor utilizando su clave, pero no al revés. Por este motivo, no se pueden repetir las claves para elementos distintos, pero sí es posible agregar, eliminar o modificar valores (Los diccionarios son mutables).
Ejemplo:


# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
