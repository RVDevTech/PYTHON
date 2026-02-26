# 1.3- Strings y sus métodos- 3. Métodos de comprobación booleana
# Definimos varias cadenas para probar los métodos
cadena1 = "Python"
cadena2 = "12345"
cadena3 = "IV"
cadena4 = "Python123"
cadena5 = "Hola Mundo!"
cadena6 = "   "  # espacios
cadena7 = "pyThon"
cadena8 = "VariableValida"
cadena9 = "python"
cadena10 = "PYTHON"

# .isalpha(): True si todos los caracteres son letras y hay al menos uno
print("cadena1.isalpha():", cadena1.isalpha())  # True
print("cadena4.isalpha():", cadena4.isalpha())  # False, contiene números

# .isdigit(): True si todos los caracteres son dígitos numéricos
print("cadena2.isdigit():", cadena2.isdigit())  # True
print("cadena3.isdigit():", cadena3.isdigit())  # False, 'IV' no es dígito

# .isdecimal(): True si todos los caracteres son dígitos en 0-9
print("cadena2.isdecimal():", cadena2.isdecimal())  # True
print("cadena3.isdecimal():", cadena3.isdecimal())  # False

# .isnumeric(): True si todos los caracteres son números (incluye romanos, superíndices, etc.)
print("cadena2.isnumeric():", cadena2.isnumeric())  # True
print("cadena3.isnumeric():", cadena3.isnumeric())  # True, 'IV' es considerado numérico

# .isalnum(): True si solo hay letras o números
print("cadena4.isalnum():", cadena4.isalnum())  # True
print("cadena5.isalnum():", cadena5.isalnum())  # False, contiene espacio y signo de exclamación

# .isprintable(): True si todos los caracteres se pueden imprimir
print("cadena5.isprintable():", cadena5.isprintable())  # True
print("cadena6.isprintable():", cadena6.isprintable())  # True, espacios son imprimibles

# .isspace(): True si la cadena contiene solo espacios, tabulaciones o saltos de línea
print("cadena6.isspace():", cadena6.isspace())  # True
print("cadena5.isspace():", cadena5.isspace())  # False

# .isascii(): True si todos los caracteres son ASCII (0-127)
print("cadena5.isascii():", cadena5.isascii())  # True
print("cadena1.isascii():", cadena1.isascii())  # True

# .islower(): True si todas las letras están en minúscula
print("cadena9.islower():", cadena9.islower())  # True
print("cadena1.islower():", cadena1.islower())  # False

# .isupper(): True si todas las letras están en mayúscula
print("cadena10.isupper():", cadena10.isupper())  # True
print("cadena1.isupper():", cadena1.isupper())    # False

# .istitle(): True si cada palabra empieza con mayúscula y el resto minúscula
print("cadena5.istitle():", cadena5.istitle())  # True, "Hola Mundo!"
print("cadena1.istitle():", cadena1.istitle())  # True, "Python"

# .isidentifier(): True si la cadena puede ser un nombre de variable válido en Python
print("cadena8.isidentifier():", cadena8.isidentifier())  # True
print("cadena5.isidentifier():", cadena5.isidentifier())  # False, contiene espacio

# .startswith(prefijo) y .endswith(sufijo)
print("cadena1.startswith('Py'):", cadena1.startswith("Py"))  # True
print("cadena1.endswith('on'):", cadena1.endswith("on"))      # True
print("cadena1.startswith('py'):", cadena1.startswith("py"))  # False, case-sensitive
print("cadena1.endswith('On'):", cadena1.endswith("On"))      # False


