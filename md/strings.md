# Strings

+++?code=assets/format_methods.py&lang=python&title="Dando formato a Strings"
@[1](Creamos nuestro String)
@[2-3](capitalize devuelve una copia de la cadena con la primera letra en mayúsculas)
@[4-5](lower devuleve una copia de la cadena en minusculas)
@[6-7](upper devuelve una copia de la cadena en mayusculas)
@[8-9](swapcase devuelve una copia de la cadena convertidas las mayúsculas en minúsculas y viceversa)

+++?code=assets/search_methods.py&lang=python&title="¿Cuantas cosas podemos comprobar en un String?"
@[1](Creamos nuestro String)
@[2-3](podemos contar la cantidad de apariciones de una subcadena)
@[4-5](O buscar donde se encuentra una determinada subcadena)
@[6-7](Con startswith podemos comprobar si nuestra cadena empieza de un determinado modo)
@[8-9](¡Y con endswith si termina!)
@[10](Redefinimos nuestra cadena)
@[11-12](¿Es nuestra cadena alfanumerica?)
@[13-14](Entonces no podrá ser alfabetica)
@[15-16](Ni numerica)
@[17](Si es todo minusculas...)
@[18-19](¡Podemos saberlo!)
@[20-21](Pero por supuesto no puede ser lo contrario a la vez)
@[22](¿Para qué sirve esto?)
@[23-24](Efectivamente tenemos solo espacios)

+++?code=assets/substitution_methods.py&lang=python&title="¿Como manipulamos estos Strings?"
@[2-3](Se puede dar formato a la cadena)
@[4-5](Sustituir partes de la cadena)
@[6-7](Y eliminar caracteres al principio y final de la cadena)
@[8-9](Tambien podemos elminar por uno de los dos sitios)
@[10-11](pero solo en el caso de que ese caracter sea el que indicamos)

+++?code=assets/union_division_methods.py&lang=python&title="¿Como manipulamos estos Strings?"
@[1-4](Con join la cadena se separa por cada uno de los elementos de un iterable)
@[5-7](Con partition obtenemos una tupla de tres elementos donde el primero es el contenido de la cadena previo al separador, el segundo, el separador mismo y el tercero, el contenido de la cadena posterior al separador)
@[8-9](Con split sin embargo una lista con todos elementos encontrados al dividir la cadena por un separador)
@[10-12](finalmente con splitlines obtendremos una lista donde cada elemento es una fracción de la cadena divida en líneas)
