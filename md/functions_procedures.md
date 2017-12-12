### Funciones, procedimientos y funciones lambda

+++?code=assets/function.py&lang=python&title="Definiendo una funci%C3%B3n"
@[6](Devolvemos un valor)

+++?code=assets/procedure.py&lang=python&title="Definiendo un procedimiento"
@[1-5](No devuelve nada)

+++?code=assets/lambda.py&lang=python&title="Definiendo una funci%C3%B3n lambda (tambien conocidas como an%C3%B3nimas)"
@[1](Se define la función)
@[2-3](Al llamarla, devuelve el valor correspondiente)
Muy útiles para implementar funciones rápidas y sencillas

+++?code=assets/map.py&lang=python&title="Funci%C3%B3n map"
@[1](Definimos una lista cualquiera)
@[2](Creamos una función lambda -de un solo parámetro- que sume 10)
@[3-5]('Con la función `map`, hacemos que se aplique la función a cada elemento de la lista. La función `map` no devuelve una lista, por lo que necesitamos envolver todo en `list`')

+++?code=assets/filter.py&lang=python&title="Funci%C3%B3n filter"
@[1](Definimos una lista cualquiera')
@[2](Creamos una función lambda -de un solo parámetro- que devuelva `boolean`)
@[3-5](Con la función `filter`, hacemos que se seleccionen de la lista aquellos elementos que devuelven `True` en la función lambda. La función `filter` no devuelve una lista, por lo que necesitamos envolver todo en `list`)

+++?code=assets/reduce.py&lang=python&title="Funci%C3%B3n reduce"
@[1](Importamos la función `reduce`. En Python 2 era nativa y no había que importarla. Guido van Rossum la odiaba xD)
@[2](Definimos una lista cualquiera')
@[3](Creamos una función lambda -de dos parámetros- que realiza la suma)
@[4-5](Con la función `reduce`, hacemos que se realice la función lambda de forma que obtengamos, en este caso, la suma de todos los elementos de la lista)
