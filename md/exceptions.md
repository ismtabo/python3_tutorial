### Excepciones

+++?code=assets/exceptions.out&lang=python&title="Lanzamiento%20y%20tratamiento%20de%20excepciones"
@[1-8](Lanzamiento de excepciones con `raise`. Podemos añadir mensaje propio a la excepción a través de su constructor)
@[10-15](Tratamiento de excepciones básica)
@[17-22](Tratamiento de excepciones obteniendo información de la excepción)
@[24-41](Se pueden tratar varias excepciones en un mismo bloque. Ordenar de más específicas a más genéricas: `ValueError` $$\subset$$ `Exception`)
@[43-51](Bloque `finally` siempre es evaluado)
@[53-69](Bloque `else` sólo se evalua si no se han lanzado excepciones)