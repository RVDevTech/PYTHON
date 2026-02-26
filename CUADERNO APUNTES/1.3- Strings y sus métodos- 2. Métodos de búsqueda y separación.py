# 1.3- Strings y sus métodos- 2. Métodos de búsqueda y separación
# Cadena original
texto = "Python es un lenguaje de programación en Python"

# .find(sub) → busca la primera aparición de 'sub'
print(".find(sub)")
print("Índice de la primera 'Python':", texto.find("Python"))   # 0
print("Índice de la primera 'Java':", texto.find("Java"))       # -1 (no existe)

# .rfind(sub) → busca la última aparición de 'sub'
print(".rfind(sub)")
print("Índice de la última 'Python':", texto.rfind("Python"))   # 42
print("Índice de la última 'Java':", texto.rfind("Java"))       # -1 (no existe)

# .count(sub) → cuenta cuántas veces aparece 'sub'
print(".count(sub)")
print("Número de veces que aparece 'Python':", texto.count("Python"))  # 2
print("Número de veces que aparece 'a':", texto.count("a"))           # 3

# .index(sub) → igual que .find(), pero lanza ValueError si no existe
print(".index(sub)")
print("Índice de la primera 'Python':", texto.index("Python"))  # 0
try:
    print("Índice de 'Java':", texto.index("Java"))
except ValueError:
    print("Error: 'Java' no está en la cadena")

# .partition(sep) → divide en tres partes por la primera aparición del separador, creando una tupla
print(".partition(sep)")
resultado = texto.partition("lenguaje")
print("Antes del separador:", resultado[0])
print("Separador:", resultado[1])
print("Después del separador:", resultado[2])

# .rpartition(sep) → divide en tres partes por la última aparición del separador
print(".rpartition(sep)")
resultado = texto.rpartition("Python")
print("Antes del último separador:", resultado[0])
print("Separador:", resultado[1])
print("Después del separador:", resultado[2])

# Slicing [start:stop:step] → extrae subcadenas
print("\nSlicing [start:stop:step]")
print("Texto completo:", texto)
print("Subcadena [0:6]:", texto[0:6])       # 'Python'
print("Subcadena [7:9]:", texto[7:9])       # 'es'
print("Subcadena [::5]:", texto[::5])       # cada 5 caracteres
print("Subcadena [-10:]:", texto[-10:])     # últimos 10 caracteres
print("Subcadena invertida [::-1]:", texto[::-1])  # cadena invertida



