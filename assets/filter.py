>>> lista = [0, -2, 30, -6, 25, 1]
>>> solo_postivos = lambda x: x > 0
>>> nueva_lista = list(filter(solo_postivos, lista))
>>> nueva_lista
[30, 25, 1]
