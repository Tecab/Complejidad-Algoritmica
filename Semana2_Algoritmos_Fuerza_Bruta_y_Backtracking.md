## 1. PROBLEMAS COMPUTACIONES

¿Qué es un problema?
- Los problemas son tareas que deben ser resueltas o cuyos objetivos de solución deben ser alcanzados.
- Existen problemas de todo nivel de complejidad: difíciles, medianamente difíciles y fáciles.
- Los informáticos resolvemos problemas a través del computador, por tanto, debemos saber diseñar algoritmos que permitan encontrar una solución óptima.

En computación, un problema lo definimos como un espacio de estados (espacio de búsqueda), que incluye:
- ESTADO INICIAL (Posición inicial) -> SOLUCIONES POSIBLES O LEGALES (Reglas aplicables (por ejemplo: Movimientos posibles)) -> ESTADO OBJETIVO (Posición final)

#### EJEMPLOS - PROBLEMAS COMPUTACIONALES
1.a. Problema 8-Puzzle
1.b. Formulación del Problema 8-Puzzle
1.a. Problema: 3 en raya
1.b. Formulación del Problema 3 en raya

## 2. ESPACIO O UNIVERSO DE BUSQUEDA

¿Qué es un espacio de búsqueda?
- Son todas las posibilidades de respuesta ante un problema, sean estas correctas o no.
- Permite encontrar la respuesta correcta a un problema (según la técnica que apliquemos).
- Los problemas de optimización también pueden ser considerados como problemas con espacio de búsqueda.

Un problema puede ser resuelto a través de:
- El análisis.
- La definición de sus características esenciales.
- La aplicación de una técnica conocida para ese problema.
Las (2) técnicas clásicas de resolución de problemas o técnicas de búsquedas son:
- Fuerza bruta (búsqueda exhaustiva)
- Backtracking

## 3. TECNICAS DE BUSQUEDAS

#### 3.1 ¿Qué es Fuerza Bruta?
- Busca sistemáticamente en todo el espacio de búsqueda.
- Es una estrategia sencilla pero a la que le hace falta sofisticación en la solución.
- Esta técnica, generalmente traduce directamente el enunciado del problema.
- Se toma la ruta más directa, sin ningún intento de minimizar el número de operaciones necesarias para calcular la solución (a lo bruto?)
- La complicación viene en poder generar todas las soluciones candidatas.
- A menudo es "suficientemente buena" especialmente para pequeñas instancias.
¿Qué es?
Una estrategia general para listar todas las opciones en un problema de Fuerza Bruta es usar permutaciones o combinaciones.

![Complejidades](/Complementos/Fuerza%20Bruta.jpeg)

Son ejemplos de Fuerza Bruta:
- La búsqueda de clasificación por selección (Selection Sort)
- La búsqueda de ordenamiento por burbuja (Bubble Sort)
- Coincidencia de cadenas (String Matching o la ocurrencia de una cadena en un texto)
  - Ejemplo #1: Buscar un producto específico en el supermercado en donde no conocemos la distribución de sus productos, solo los tipos de productos.
  - Ejemplo #2: Encontrar cierto elemento en una vector de tamaño n, asumir que el vector no está ordenado.
  - Ejemplo #3: Implementar la ordenación por selección:
    - Buscar el mínimo elemento de la lista
    - Intercambiarlo con el primero
    - Buscar el siguiente mínimo en el resto de la lista
    - Intercambiarlo con el segundo

#### 3.2 ¿Qué es Backtracking?
- BACKTRACKING es una técnica para buscar sistemáticamente a través de todas las configuraciones de un espacio de búsqueda.
- Para esto se construye todas las posibles soluciones candidatas de manera sistemática.
- Dada una solución candidata S, se procede a: 
   - Verificar si S es solución. Si lo es, hacen algo con ella (depende del problema).
   - Construyen todas las posibles extensiones de S, e invocan recursivamente al algoritmo con todas ellas.

## 4. VENTAJAS Y DESVENTAJAS DEL BACKTRACKING

#### VENTAJAS: 
- El Backtracking puede resolver casi cualquier problema, debido a su naturaleza de fuerza bruta.
- Se puede utilizar para encontrar todas las soluciones existentes si existe algún problema.
- Es una representación paso a paso de una solución a un problema dado, que es muy fácil de entender.
- Muy fácil de escribir el código y también de depurar.

#### DESVENTAJAS: 
- Es muy lento en comparación con otras soluciones.
- Dependiendo de los datos que tenga, existe la posibilidad de realizar una búsqueda muy grande con Backtracking y al final no encontrar ninguna coincidencia con sus parámetros de búsqueda.
- Costo computacional muy alto, Backtracking es un algoritmo recursivo que consume mucho de la memoria y del procesador.
- Considerar usar el algoritmo de ramificación y poda (para gran volumen de datos, consume menos recursos a un coste de tiempo menor).

## 5. CONCLUSIONES

- El espacio de búsqueda es el conjunto de todos los estados posibles (SOLUCIONES) para un problema dado.
- Técnicas de búsqueda son las formas de tratar el espacio de búsqueda.
  - Fuerza bruta
  - Backtracking
- La Complejidad Algorítmica variará de acuerdo a la técnica utilizada y el tamaño del espacio de búsqueda (cantidad de posibles soluciones).
