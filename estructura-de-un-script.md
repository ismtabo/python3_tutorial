# Estructura de un script

Pongamos el caso del siguiente código de ejemplo python:

```python
#! /usr/bin/env python3

print("Hello World")
```

Se puede observar que a diferencia de otros lenguajes como **C**, **Java**, **Go**, **Rust**, etc. **Python** no necesita una función principal que ejecutarse, sino que irá evaluando las sentencias que encuentre en el fichero de script.

En este caso, la primera línea:
```python
#! /usr/bin/env python3
```

Indica al SO el intérprete que deberá utilizar para el _script_. En caso de que no queramos utilizar un intérprete para ejecutar el fichero, podremos hacerlo, en sistemas UNIX, indicando dicho intérprete y dando permisos de ejecución al fichero de la siguiente forma:
```
$ chmod +x hello_world.py
$ ./hello_world.py
"Hello World"
```
