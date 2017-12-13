### Generadores, iteradores y _list comprehensions_

+++?code=assets/iterators.out&lang=python&title="Iteradores"
@[1-12](Iteración sobre una lista mediante bloque `for`)
@[13-14](Extracción de un iterador de una lista)
@[15-26](Avance del iterador sobre los elementos de la lista: `next(iterator [, default])`)
@[27-30](Al agotar los elementos de la lista salta la excepción `StopIteration`)
@[31](Es necesario reinicilizar el iterador para volver obtener los elementos de la lista)
@[32-38](Al utilizar un defecto, no salta `StopIteration`)

+++?code=assets/iterators_common_use.py&lang=python&title="Uso habitual de iteradores"

+++?code=assets/generator_yield.out&lang=python&title="Generadores%20%60yield%60"
@[2-10](Definición de función generadora)
@[13](Asignación de función a una variable)
@[14-33](El comportamiento es igual que el de un iterador)

+++?code=assets/list_comprehension.out&lang=python&title="List comprehension y generadores"
@[1-4](_List comprehension_ para generación de listas. Equivalencia con uso de `map` y `filter`)
@[5-6](_List comprehension_ para generación de conjuntos)
@[7-8](_List comprehension_ para generación de diccionarios)
@[9-10](Al utilizarlo entre paréntesis devuelve un generador, **NO** una tupla)
@[11-12](Forma correcta de generar una tupla con _list comprehension_)
@[13-14](Puede usarse en vez de un iterable)
@[15-18](`all(iterable)` y `any(iterable)` son funciones lógicas sobre elementos iterables. _Para todos_ y _Existe al menos uno_, respectivamente)
@[19-26](Ejemplo de uso de un generador en un bloque `for`)
