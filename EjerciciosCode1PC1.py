"""
Utilizando la técnica de fuerza bruta:

Dado un arreglo de números, imprime todos los posibles pares de números cuya suma sea igual a X.
  ej: 
    Arreglo: [1, 2, 3, 4, 5, 6, 8]
    X: 9

    Respuestas:
      1 8
      3 6
      4 5
"""

def all_pairs_that_sum(arreglo, numero):
  answers = []

  # for (int i = 0; i < n - 1; ++i)
  for i in range(len(arreglo) - 1):
    primer_numero = arreglo[i]

    # for (int j = i + 1; j < n; ++j)
    for j in range(i + 1, len(arreglo)):
      segundo_numero = arreglo[j]

      if primer_numero + segundo_numero == numero:
        answers.append([primer_numero, segundo_numero])

  return answers


arregloejem=[1, 2, 3, 4, 5, 6, 8]
arregloejem2=[5, 5, 10, 0, 14, 15, 20, -5]

print(all_pairs_that_sum(arregloejem, 9))
# Output: [[1, 8], [3, 6], [4, 5]]

print(all_pairs_that_sum(arregloejem2, 10))
# Output: [[5, 5], [10, 0], [15, -5]]


"""Utilizando la técnica de backtracking: """

def find_pairs_with_sum(arr, target_sum):
    def backtrack(start, current_sum, current_pair):
        if current_sum == target_sum and len(current_pair) == 2:
            pairs.append(current_pair[:])
            return
        if current_sum >= target_sum or start == len(arr):
            return

        for i in range(start, len(arr)):
            current_pair.append(arr[i])
            backtrack(i + 1, current_sum + arr[i], current_pair)
            current_pair.pop()

    pairs = []
    backtrack(0, 0, [])
    return pairs

# Ejemplo de uso
arreglo = [1, 2, 3, 4, 5, 6, 8]
X = 9
resultado = find_pairs_with_sum(arreglo, X)

for pair in resultado:
    print("-",pair[0], pair[1])
