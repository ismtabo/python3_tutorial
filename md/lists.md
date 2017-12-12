### Listas y operaciones sobre Listas

+++?code=assets/lists_and_appends.py&lang=python&title="Creando y agregando elementos"
@[1](Así creamos una lista)
@[2](Con `append` añadimos un elemento al final)
@[1-4](Observa como ha quedado la lista tras añadir el elemento al final)
@[5](Con `extend` añadimos los elementos de otra lista al final)
@[4-7](Observa como ha quedado la lista tras añadir los elementos al final)
@[8](Con `insert` indicamos que inserte en la posición 1 el numero 39)
@[7-10](Observa como ha quedado la lista tras insertar el elemento en la posición indicada)

+++?code=assets/list_deletion.py&lang=python&title="Eliminado elementos"
@[2-3](Con `pop` eliminamos el último elemento, que es retornado)
@[1-2,4-5](Observa como ha quedado la lista tras eliminar el último elemento)
@[6-7](Si a `pop` le indicamos un número entero , le estamos diciendo que elimine el elemento en tal posición)
@[5-6,8-9](Observa como ha quedado la lista tras eliminar el elemento con índice especificado)
@[10](Con `remove` indicamos que elimine la primera aparición del elemento especificado)
@[9-12](Observa como ha quedado la lista tras eliminar la primera aparición del elemento especificado)

+++?code=assets/list_access.py&lang=python&title="Accediendo a los elementos"
@[1-3](Con los corchetes accedemos a los elementos que indicamos)
@[1,4-5](Como puedes ver, es similar a otros lenguajes)
@[1,6-7](Pero aquí empieza la magia: fíjate en este acceso. Así de fácil es acceder al último elemento)
@[1,8-9](Y fíjate también en este)
@[1,6-9](Si ponemos indices negativos, estamos accediendo desde la parte final de la lista)
@[1,10-11](También podemos extraer trozos de la lista. En este caso desde el índice 1 inclusive, hasta el índice 3 exclusive)
@[1,12-13](Así accedemos desde el índice 1 inclusive, hasta el final)
@[1,14-15](Y así, accedemos desde el inicio de la lista hasta el índice 2 exclusive)
@[1,16-17](También podemos extraer saltando elementos, como en este caso de dos en dos)
@[1,18-19](Invertir el orden de la lista es tan fácil como esto)
@[1,20-21](Y también podemos acceder de forma salteada y desde el final hasta el inicio)
