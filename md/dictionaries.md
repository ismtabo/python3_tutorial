### Diccionarios

Un **diccionario** en Python, es una **colección de pares clave-valor**. Lo que normalmente consideraríamos un _tabla hash_ o matriz asociativa.

Las **claves** consisten en valores de cualquier tipo inmutable de los que hayamos visto: números, _strings_, tuplas... Dichas **claves** deben ser únicas, ya que al agregar un nuevo valor con la misma clave, se sobrescribirá el anterior.

+++?code=assets/dictionaries_creation.out&lang=python&title="Creaci%C3%B3n%20y%20uso%20b%C3%A1sico%20de%20diccionarios"
@[1-5](Inicialización de diccionarios)
@[6-10](Acceso a elementos de un diccionario)
@[11-14](Acceso fallido a un diccionario. Error `KeyError`)
@[15-16](Saber si una clave está en un diccionario)
@[17-18](Acceso a elementos de un diccionario con valor por defecto: : `get(key [, default])`)
@[19-22](Sacar elementos de un diccionario: `pop(key [, default])`)
@[23-25](Actualización de un diccionario a través de otro: `update([other, ]**kwargs)`)
@[26-28](Eliminación de elementos de un diccionario según clave)
@[29-31](Vaciar diccionario)

+++?code=assets/dictionaries_iteration.out&lang=python&title="Iteraci%C3%B3n%20sobre%20elementos%20e%20un%20diccionario"
@[2-3](Número de elementos que contiene un diccionario)
@[4-5](Iterable de las claves de un diccinario)
@[6-7](Iterable de los valores de un diccionario, ordenados por clave)
@[8-9](Iterable de los pares clave valor de un diccionario)
@[10-13](Ejemplo de iteración sobre pares mediante un bloque `for`)
