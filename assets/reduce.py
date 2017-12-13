>>> from functools import reduce
>>> lista = [1, 2, 3, 4]
>>> suma = lambda x, y: x + y
>>> reduce(suma, lista)
10
