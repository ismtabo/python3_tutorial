miString = "Soy una cadena una cadena String 100"
miString.count("una cadena")
>>> 2
miString.find("una")
>>> 16
miString.startswith("Soy")
>>> True
miString.endswith("Soy")
>>> False
miString = "micadenaalfanumerica288"
miString.isalnum()
>>> False
miString.isalpha()
>>> False
miString.isdigit()
>>> False
miString = "soytodominusculas"
miString.islower()
>>> False
miString.isupper()
>>> False
miString = "    "
miString.isspace()
>>> True
