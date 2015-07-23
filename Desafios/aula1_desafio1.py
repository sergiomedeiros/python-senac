# imprima uma lista com numeros pares de 0 a 10

lista = list(range(100))
lista = [ i  for i in lista if i % 2 == 0]
print(lista)
