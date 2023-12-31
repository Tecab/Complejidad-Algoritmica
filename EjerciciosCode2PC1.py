"""
Utilizando la técnica de recursión:

Dada una lista que puede contener números enteros u otras listas (que pueden contener números enteros
u otras listas con las mismas condiciones), determine la suma total de todos los números enteros.

ej.
  Números: [[[1]], [[[[4]]]], 7, 0, [[2, 3], 5, [3, 2]]]
  Respuesta: 1 + 4 + 7 + 0 + 2 + 3 + 5 + 3 + 2 = 27

  Números: [1, 1, 1, 1, [2, [3], [4], [0, -8]]]
  Respueta: 5
"""

def get_sum_from(numbers):
  def recursion(index, array):
    if index >= len(array):
      return 0
    ans = 0
    if type(array[index]) == list:
      ans = recursion(0, array[index])
    else:
      ans = array[index]
    return ans + recursion(index + 1, array)
  return recursion(0, numbers)

print(get_sum_from([[[1]], [[[[4]]]], 7, 0, [[2, 3], 5, [3, 2]]]))
# Output: 27

print(get_sum_from([1, 1, 1, 1, [2, [3], [4], [0, -8]]]))
# Output: 5