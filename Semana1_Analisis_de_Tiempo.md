## 1. EFICIENCIA DE UN ALGORITMO

- **HECHOS:** Los algoritmos resuelven problemas
  - No hay una sola forma de resolver un problema, y no todas las soluciones son las mejores.
  - No todas las soluciones son capaces de utilizar eficientemente nuestros recursos.
  - Por lo tanto, necesitamos encontrar la mejor y más eficiente solución a un problema antes de actuar.

En Programación:
- No podemos dejar sujeto a conjeturas, debemos encontrar el mecanismo para encontrar la mejor solución.
- Necesitamos un estándar claro para evaluar la eficiencia de nuestros algoritmos.
- Aquí es donde interviene el concepto de complejidad algorítmica, que nos ayuda a determinar la eficiencia de un algoritmo en función de los recursos necesarios.

La complejidad algorítmica es una métrica teórica que nos ayuda a describir el comportamiento de un algoritmo cuando pasa del mejor de los casos al peor de los casos, en términos de:

- Tiempo de ejecución (tiempo que tarda un algoritmo en resolver un problema)
- Memoria requerida (cantidad de memoria necesaria para procesar las instrucciones que solucionan dicho problema).

Aquí es donde intervienen los conceptos de complejidad temporal y espacial, que nos ayudan a determinar la eficiencia del algoritmo en función de los recursos necesarios.

La complejidad algorítmica nos ayuda a comparar entre la efectividad de un algoritmo y otro, y decidir cuál es el que nos conviene implementar.

## 2. COMPLEJIDAD TEMPORAL VS COMPLEJIDAD ESPACIAL

- **Complejidad Temporal (Tiempo de ejecución)**
  - Debemos tener en cuenta que los problemas que debamos resolver mediante el uso de algoritmos, sean capaces de encontrar una solución en el tiempo esperado.
  - Esta solución la expresaremos mediante una función T que recibe un input al que llamaremos n 
  - T(n) = Tiempo que tardará nuestro algoritmo

- **Complejidad Espacial (Memoria requerida)**
  - Conocer cuantos recursos (espacio en memoria) necesitaremos para resolver un problema a través de un algoritmo.

Estos valores se encuentran en función del tamaño del problema (valor o valores dictados por el número de elementos con los que un algoritmo trabaja, pero a veces no….)

## 3. APROXIMACIONES A LA FUNCION DE TIEMPO T(n)

#### COMPLEJIDAD TEMPORAL: ¿Cómo podríamos aplicar la función T(n)?

1. Cronometrando el tiempo en el que se ejecuta un algoritmo
   - Calcular el tiempo en el que se ejecuta un algoritmo. Sin embargo, no es una buena forma de medir los algoritmos, ya que no se puede predecir cuánto demorará a medida que crecen nuestros pasos (instrucciones). Y las diferencias de tiempo dependerán de varios factores:
     - La velocidad de los CPU utilizados (¿tardará lo mismo en ejecutarse en un procesador Pentium III que en un Octacore i7?).
     - Otros procesos que esté ejecutando el sistema operativo.
     - Los distintos lenguajes de programación utilizados (¿un código en JavaScript demorará lo mismo que uno en C++?).
   - Para una medida temporal, simplemente calculamos la diferencia del tiempo previo y posterior de la ejecución del algoritmo
     - La complejidad del tiempo no se trata de cuántos segundos lleva ejecutar el algoritmo.
     - Se trata de medir el número de operaciones que se ejecutan.
     - Estas operaciones se ven afectadas por el tamaño de la entrada y cómo se organizan sus elementos.

2. Contando los pasos con una medida abstracta de operación
   - Cada operación aritmética, comparaciones, asignaciones, etc. que ejecute el algoritmo será contabilizada.

ENTONCES:
- Solo la complejidad temporal: “No llega a ser una buena métrica para evaluar la efectividad de un algoritmo, ya que parece obvio que cierto algoritmo tardará la mitad de tiempo en ejecutarse en un procesador lo doble de rápido….”
- La medición del crecimiento de nuestra función: Debería estar libre de aquellos términos que no son relevantes para poder medir el algoritmo (y que son variables en el polinomio). Para lograrlo, nos introducimos a la Notación Asintótica.

## 4. NOTACION ASINTOTICA - NOTACION BIG O

Crecimiento Asintótico: significa que conforme se va hacia el infinito o el input en un algoritmo crece hacia el infinito.
Características:
- No importan las variaciones pequeñas dentro de la ecuación.
- El enfoque se centra en lo que sucede conforme el tamaño del problema se acerca al infinito.
- Se tiene que tener en cuenta el mejor de los casos, promedio, peor de los casos. Para medir el algoritmo, consideramos el peor de los casos.
- Usando la notación Big O únicamente importa el término de mayor tamaño (dentro de la ecuación), esto es, el término que crece más rápido.

## 5. CLASES DE COMPLEJIDAD ALGORITMICA
Existen distintos tipos o clases de complejidad algorítmica (llamados también orden de complejidad).
En la siguiente tabla se agrupan todas las complejidades que crecen de igual forma, es decir, que pertenecen al mismo orden.

![Complejidades](/Complementos/Notacion%20Big%20O.jpeg)


## CONCLUSIONES
- La complejidad algorítmica o ritmo de crecimiento es una métrica que nos permite como programadores evaluar la factibilidad de las diferentes soluciones de un problema, y poder decidir con un argumento matemático cuál es mejor mediante comparaciones.
- Este tipo de herramienta teórica cobra importancia cuando se trabaja con Big Data, Machine Learning o hardware con recursos muy limitados como Arduino donde la optimización es crucial.
- Se cree que la complejidad algorítmica tiene aparentemente poca utilidad en el día a día de un programador habitual (que tiene poca importancia a nivel práctico), pero definitivamente, quien la domina, adquiere competencias que algunas empresas valoran mucho y solicitan.
- La complejidad algorítmica nos permite dimensionar y pensar acerca del comportamiento de nuestras soluciones y la manera en la que se codifica, y no solo codear un algoritmo que termine costándonos más en un futuro.
- Deberemos elegir aquellos algoritmos que se comportarán mejor al crecer los datos de entrada.
