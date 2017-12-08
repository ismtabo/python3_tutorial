# Python 3
## Qué puedo hacer

---

# Qué vamos a ver

- Un poco de Python, ¿qué es?
- Los falsos mitos de Python
- Facilitándonos el trabajo
- Utilidades prácticas
    - Tipos de datos básicos, Strings, Bytes y Bytesarray
    - La utilidad de las distintas colecciones: Listas, Tuplas, Diccionarios, Conjuntos
    - Control de flujo con condiciones y bucles
    - Definición de funciones y funciones _lambda_
    - List comprehension y generadores, un paso más allá
    - Entrada y salida por terminal y con ficheros
    - Excepciones

---

# Un poco de Python, ¿qué es?

- Es un lenguaje de programación de (muy) alto nivel
- Es un lenguaje interpretado
- Es un lenguaje multiparadigma
- Es fuertemente tipado pero dinámico
- Favorece la lectura de código
- Obliga a la estructuración visual de código

+++

# Un poco de Python, ¿qué es? II

- Es multiplataforma
- Open Source ([PSFL](http://es.wikipedia.org/wiki/Python_Software_Foundation_License))

---

# Falsos mitos de Python

- Python es lento
    - Permite llamadas nativas a funciones de C/C++
    - PyPI -> Python implementado en Python
- Poca capacidad de desarrollar aplicaciones completas
    - openERP, parte del Kernel de Linux, Instagram, ...

---

# Facilitándonos el trabajo - `Setuptools`

`Setuptools`, es una colección de mejoras para el módulo `disutils` de Python.
- Por defecto, utiliza PyPI para buscar paquetes
- Permite crear paquetes Egg Pythok que son módulos de Python empaquetados en un sólo archivo para su distribución
- Incluye archivos de configuración y todos los archivos que forman parte del dicercotrio de tragajo, sin necesidad de listarlos individualmente o crear archivos de manifiesto

+++

# Facilitándonos el trabajo - `Easyinstall`

`easy_install`, es una herramienta que se basa en `Setuptools` para automáticamente encontrar y descargar desde Internet las dependencias, para instalarlas o actualizarlas, ya sea bajo demanda o cuando son requeridas como dependencias al instalar otra aplicación
- Instalación en sistemas Debian
    `sudo apt-get install build-essential python-dev python-setuptools`
- Ejemplos de uso
    - `easy_install SQLObject`
    - `easy_install -f http://pythonpaste.org/package_index.html SQLObject`
    - `easy_install -i http://pypi.ejemplo.com/simple SQLObject (replica repositorio)`
    - `easy_install http://ejemplo.com/ruta/a/MiPaquete-1.2.3.tgz`
    - `easy_install ./Descargas/OtroPaquete-3.2.1-py2.7.egg`
    - `easy_install "ZopeSkel==2.21.2“ (versión especifica)`
    - `easy_install --upgrade PyProtocols`

+++

# Facilitándonos el trabajo - `Python Package Index`

`pip` es un sistema de gestión de paquetes que facilita la instalación y administración de paquetes de software escritos en Python. Estos paquetes pueden encontrarse en [Python Package Index](https://pypi.python.org/pypi).

Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen `pip` (`pip3` para Python3) por defecto.

- Instalación en sistemas Debian
    `sudo apt-get install build-essential python-pip python3-pip`
- Ejemplos de uso
    - `pip install nombre-paquete`
    - `pip uninstall nombre-paquete`
    - `pip install -r requirements.txt`
    - `pip${versión} install nombre-paquete`

+++

# Facilitándonos el trabajo - `Virtualenv`

`virtualenv` es una herramienta de desarrollo en Python escrita por Ian Bicking y usada para crear entornos aislados para Python, en los que es posible instalar paquetes sin interferir con otros virtualenvs ni con los paquetes de Python del sistema.

- Inslatación en sistemas Debian
    `sudo apt-get install build-essential virtualenv`
- Ejemplo de uso
    - Creación de entorno virtual: `$ virtualenv mi_env`
    - Activar el entorno virtual: `$ source mi_env/bin/activate`
    - Trabajar en el entorno virtual: `(mi_env)$ pip install django`
    - Salir del entorno virtual: `(mi_env)$ deactivate`

`virtualenvwrapper` es una herramienta que permite una interacción más cómoda con los entornos virtuales.
