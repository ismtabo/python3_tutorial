# Python 3
## Qué puedo hacer

---

### Qué vamos a ver

- Un poco de Python, ¿qué es?
- Los falsos mitos de Python
- Facilitándonos el trabajo
- Utilidades prácticas
    - Tipos de datos básicos, Strings, Bytes y Bytesarray
    - La utilidad de las distintas colecciones: Listas, Tuplas, Diccionarios, Conjuntos
    - Control de flujo con condiciones y bucles
    - Definición de funciones y funciones _lambda_

+++

### Qué vamos a ver II

- Utilidades prácticas
    - List comprehension y generadores, un paso más allá
    - Entrada y salida por terminal y con ficheros
    - Excepciones

---

### Un poco de Python, ¿qué es?

- Es un lenguaje de programación de (muy) alto nivel
- Es un lenguaje interpretado
- Es un lenguaje multiparadigma
- Es fuertemente tipado pero dinámico
- Favorece la lectura de código
- Obliga a la estructuración visual de código

+++

### Un poco de Python, ¿qué es? II

- Es multiplataforma
- Open Source ([PSFL](http://es.wikipedia.org/wiki/Python_Software_Foundation_License))

---

### Falsos mitos de Python

- Python es lento
    - Permite llamadas nativas a funciones de C/C++
    - PyPI -> Python implementado en Python
- Poca capacidad de desarrollar aplicaciones completas
    - openERP, parte del Kernel de Linux, Instagram, ...

---

### Facilitándonos el trabajo - `Setuptools`

`Setuptools`, es una colección de mejoras para el módulo `disutils` de Python.
- Por defecto, utiliza PyPI para buscar paquetes
- Permite crear paquetes Egg Pythok que son módulos de Python empaquetados en un sólo archivo para su distribución
- Incluye archivos de configuración y todos los archivos que forman parte del dicercotrio de tragajo, sin necesidad de listarlos individualmente o crear archivos de manifiesto

+++

### Facilitándonos el trabajo - `Easyinstall`

`easy_install`, es una herramienta que se basa en `Setuptools` para automáticamente encontrar y descargar desde Internet las dependencias, para instalarlas o actualizarlas, ya sea bajo demanda o cuando son requeridas como dependencias al instalar otra aplicación

+++

### Facilitándonos el trabajo - `Easyinstall` II

- Instalación en sistemas Debian
    `sudo apt-get install build-essential python-dev python-setuptools`
- Ejemplos de uso
    - `easy_install SQLObject`
    - `easy_install -f http://pythonpaste.org/package_index.html SQLObject`
    - `easy_install -i http://pypi.ejemplo.com/simple SQLObject (replica repositorio)`

+++

### Facilitándonos el trabajo - `Python Package Index`

`pip` es un sistema de gestión de paquetes que facilita la instalación y administración de paquetes de software escritos en Python. Estos paquetes pueden encontrarse en [Python Package Index](https://pypi.python.org/pypi).

Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen `pip` (`pip3` para Python3) por defecto.

+++

### Facilitándonos el trabajo - `Python Package Index` II

- Instalación en sistemas Debian
    `sudo apt-get install build-essential python-pip python3-pip`
- Ejemplos de uso
    - `pip install nombre-paquete`
    - `pip uninstall nombre-paquete`
    - `pip install -r requirements.txt`
    - `pip${versión} install nombre-paquete`

+++

### Facilitándonos el trabajo - `Virtualenv`

`virtualenv` es una herramienta de desarrollo en Python escrita por Ian Bicking y usada para crear entornos aislados para Python, en los que es posible instalar paquetes sin interferir con otros virtualenvs ni con los paquetes de Python del sistema.

+++

### Facilitándonos el trabajo - `Virtualenv` II

- Inslatación en sistemas Debian
    `sudo apt-get install build-essential virtualenv`
- Ejemplo de uso
    - Creación de entorno virtual: `$ virtualenv mi_env`
    - Activar el entorno virtual: `$ source mi_env/bin/activate`
    - Trabajar en el entorno virtual: `(mi_env)$ pip install django`
    - Salir del entorno virtual: `(mi_env)$ deactivate`

`virtualenvwrapper` es una herramienta que permite una interacción más cómoda con los entornos virtuales.

---

### Tipos de datos

<table style="border-collapse:collapse;border-spacing:0;border-color:#ccc;margin:0px auto"><tr><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#f0f0f0">Tipo</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#f0f0f0">Clase</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#f0f0f0">Notas</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#f0f0f0">Ejemplo</th></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">`str`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">Cadena</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">Inmutable. Se pueden iniciar con `'`, `"` o `"""` (multilínea)<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">`'string'`<br></td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">`int`<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">Entero</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">Precisión arbitraria<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff">`42` ó `2e10`<br></td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`float`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Real<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Coma flotante de doble precisión<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`3.14` ó `'inf'`<br></td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`complex`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Complejo</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Parte real y parte imaginaria `j`<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`(4.5 + 3j)`</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`bool`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Booleano</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Valor booleano, subclase de `int`<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`True` ó `False`<br></td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`list`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Secuencia</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Mutable, puede contener objetos de diversos tipos<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`[4.0, 'string', True]`<br></td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`tuple`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Secuencia</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Inmutable, puede contener objetos de diversos tipos<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`(4.0, 'string', True)`</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`set`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Conjunto</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Mutable, sin orden, no contiene elementos duplicados<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`set([4.0, 'string', True])` ó `{4.0, 'string', True}`</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`fronzenset`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Conjunto</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Inmutable, sin orden, no contiene elementos duplicados<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`frozenset([4.0, 'string', True])`</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`dict`</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Mapping</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">Grupo de pares `key: value`<br></td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;vertical-align:top">`{'key1': 1.0, 'key2': False}`<br></td></tr></table>

---

### Estructuras de control de flujo

+++?code=assets/relations_operators.out&lang=python&title="Operadores relacionales (de comparación)"
@[1-2](Igualdad: `==`)
@[3-4](Diferencia: `!=`)
@[5-6](Menor que: `<`)
@[7-8](Mayor que: `>`)
@[9-10](Menor o igual que: `<=`)
@[11-12](Mayor o igual que: `>=`)
@[13-16](Igualdad de referencia: `is`)
@[17-18](Pertenencia: `in`)

+++?code=assets/logic_operators.out&lang=python&title="Operadores lógicos"

+++ 

### Estructuras de control de flujo

#### Estructuras de control de flujo condicionales

<small>
Las estructuras de control de flujo condicionales, se definen mediante el uso de tres palabras claves reservadas, del lenguaje: `if`(si), `elif`(sino, si) y `else` (sino).
</small>

+++?code=./assets/if_elif_if.py&lang=python&title="Estructuras de control de flujo condicionales"
@[1-2](`if` block)
@[3-4](`elif` block)
@[5-6](`else` block)
