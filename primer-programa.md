# Primer programa

En este tutorial vamos a utilizar las versiones 3.X de Python, disponible en https://www.python.org/downloads/. Es posible que en algunos sistemas operativos no esté disponible, tales como Windows o en sistemas UNIX/Linux como Gentoo. En sistemas como distribuciones basadas en Debian/Ubuntu y en OSX estará instalado ya que algunas funcionalidades del sistema operativo, estarán programadas en este lenguaje, y en particular en la versión 3.

## Hello world en el intérprete

Para entrar en contacto con el intérprete, vamos a escribir la siguiente sentencia:

```python
"Hello World!"
```

Como se puede observar, al introducirlo en el intérprete y dar al intro, la salida del intérprete será la siguiente.

```python
>>> "Hello World!"
"Hello World!"
```

Esto se debe a que después de cada sentencia introducida, si esta devolviese algún valor, dicho valor se mostrará en la línea siguiente. Al igual que si utilizásemos la función para imprimir por entrada estándar `print`:

```python
>>> print("Hello World!")
"Hello World!"
```

## Hello world en un fichero

Este mismo código lo podemos escribir en un fichero con extensión `.py`:

Contenido de `hello_world.py`:
```python
print("Hello World!")
```

Posteriormente para ejecutar dicho programa usaremos la siguiente sentencia en nuestro terminal:
```
$ python3 hello_world.py
"Hello World!"
```

A los ficheros con extensión `.py` con lenguaje **Python**, se les llama **scripts**, al igual que los ficheros de otros lenguajes como **Bash**.