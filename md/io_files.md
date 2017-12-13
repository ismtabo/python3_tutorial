### Entrada/Salida estándar y mediante ficheros

+++?code=assets/stdout.out&lang=python&title="Salida%20est%C3%A1ndar"
@[1-2](Impresión por salida estándar mediante: `print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`)
@[3-6](Impresión de todo tipo de variables (Las instancias de objetos tendrán nombre de la clase y dirección de memoria))
@[7-13](Uso de `*args` en la función `print`)
@[14-15](Efecto del parámetro `end`)
@[17-20](Salida formateada mediante el uso de `%` y `format`. Más información en: [pyformat](https://pyformat.info/))
@[21-23](Salida a través de salida estándar de error `2>`)

+++?code=assets/stdin.out&lang=python&title="Entrada%20est%C3%A1ndar"
@[1-3](Entrada estándar (lee hasta salto de línea))
@[4-6](Casting sobre entrada estándar)
@[7-11](Error al hacer _casting_ inválido, salta excepción `ValueError`)
@[12-15](Ejemplo con _promp_ y asignación a una variable)
@[17-26](Uso de `sys.stdin` para iterar sobre entrada estándar `<`)

+++?code=assets/files.out&lang=python&title="Ficheros"
@[1](Ejemplo de apertura de fichero: `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`)
@[1-8](Ejemplo de escritura de fichero. No olvidar `.close()` final)
@[10-17](Ejemplo de lectura desde un fichero)
@[19-22](Para tener un acceso más seguro, es mejor utilizar contextos)

+++
#### Significado de modos de apertura

```python
"""
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
========= ===============================================================
"""
```
