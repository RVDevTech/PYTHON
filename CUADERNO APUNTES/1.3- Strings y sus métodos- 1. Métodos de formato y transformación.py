# 1.3- Strings y sus métodos- 1. Métodos de formato y transformación

# Cadena original, ininmutable
texto = "  Hola Mundo! Esto es Python"

# 1. Convertir a minúsculas
print("\n.lower():", texto.lower())

# 2. Convertir a mayúsculas
print(".upper():", texto.upper())

# 3. Primera letra de cada palabra en mayúscula
print(".title():", texto.title())

# 4. Primera letra de la cadena en mayúscula
print(".capitalize():", texto.capitalize())

# 5. Invertir mayúsculas y minúsculas
print(".swapcase():", texto.swapcase())

# 6. Aplanar caracteres a minúsculas (más agresivo)
print(".casefold():", texto.casefold())

# 7. Eliminar espacios o caracteres indicados al inicio y final
print(".strip():", texto.strip())
print(".strip('!'):", texto.strip("!"))

# 8. Eliminar espacios o caracteres solo al inicio
print(".lstrip():", texto.lstrip())

# 9. Eliminar espacios o caracteres solo al final
print(".rstrip():", texto.rstrip())

# 10. Alinear a la izquierda con relleno
print(".ljust(40, '*'):", texto.ljust(40, '*'))

# 11. Alinear a la derecha con relleno
print(".rjust(40, '-'):", texto.rjust(40, '-'))

# 12. Centrar en un ancho con relleno
print(".center(40, '='):", texto.center(40, '='))

# 13. Rellenar con ceros a la izquierda
numero = "42"
print(".zfill(5):", numero.zfill(5))

# 14. Reemplazar texto
print(".replace('Python', 'PYTHON'):", texto.replace("Python", "PYTHON"))
print(".replace('o', '0', 2):", texto.replace("o", "0", 2))  
# solo los 2 primeros
# 15. Eliminar prefijo
texto_pref = "Pythonista"
print(".removeprefix('Py'):", texto_pref.removeprefix("Py"))

# 16. Eliminar sufijo
texto_suf = "Hola.py"
print(".removesuffix('.py'):", texto_suf.removesuffix(".py"))

# 17. Expandir tabulaciones
texto_tab = "Col1\tCol2\tCol3"
print(".expandtabs(4):")
print(texto_tab.expandtabs(4))
print(".expandtabs(8):")
print(texto_tab.expandtabs(8))