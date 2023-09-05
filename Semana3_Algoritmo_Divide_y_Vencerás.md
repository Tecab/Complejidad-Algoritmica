## 1. DEFINICIÓN ALGORITMO DIVIDE Y VENCERÁS

**¿Cómo definimos este algoritmo?**
- El algoritmo Divide y Vencerás tiene una estructura recursiva.
- Para resolver el problema dado, se llama a sí mismo recursivamente una o más veces para tratar subproblemas estrechamente relacionados.
- El algoritmo divide y vencerás implica tres pasos en cada nivel de recursividad.
  - Dividir: dividir el problema en varios subproblemas que son similares al problema original pero más pequeños,
  - Conquistar: resolver el subproblema recursivamente, y si los tamaños del subproblema son lo suficientemente pequeños, resuelva directamente los subproblemas.
  - Combinar: combinar esta solución para crear una solución al problema original.

## 2. EJEMPLOS

![Ejemplo1](/Complementos/Ejemplo1.jpeg)
![Ejemplo2](/Complementos/Ejemplo2.jpeg)
![Ejemplo3](/Complementos/Ejemplo3.jpeg)
![Ejemplo4](/Complementos/Ejemplo4.jpeg)

## 3. COMPLEJIDAD ALGORÍTMICA

La complejidad del tiempo para el algoritmo Divide y Vencerás se calcula utilizando el teorema maestro.

T(n) = aT(n / b) + f(n)

Donde:
- **n** es el tamaño de entrada
- **a** es el número de subproblemas en la recursividad
- **n/b** es el tamaño de cada subproblema donde se supone que todos los subproblemas tienen el mismo tamaño. 

Podemos decir que f(n) es el trabajo realizado fuera de la llamada recursiva.

![CA](/Complementos/CA.jpeg)
![CA2](/Complementos/CA2.jpeg)
