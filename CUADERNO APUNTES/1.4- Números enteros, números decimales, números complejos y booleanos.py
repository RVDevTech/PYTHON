# 1.4 – Números enteros, números decimales, números complejos y booleanos
# a) Números enteros (int)
entero = 42
neg_entero = -15

# Representaciones en distintas bases
print("Binario:", bin(entero)) # Conversión binaria
print("Octal:", oct(entero)) # Conversión octal
print("Hexadecimal:", hex(entero)) # Conversión hexadecimal
# Enteros decimales en otras bases (Python ya los interpreta como int)
print("Decimal desde literal binario 0b1010:", 0b1010) # Impresión entera decimal desde binaria
print("Decimal desde literal octal 0o12:", 0o12)  # Impresión entera decimal desde octal
print("Decimal desde literal hexadecimal 0xA:", 0xA) # Impresión entera decimal desde octal
# Funciones globales relacionadas
print("Valor absoluto:", abs(neg_entero)) # Eliminación del signo
print("Divmod (10, 3):", divmod(10, 3)) # División con cociente y resto
print("Potencia (2**5):", pow(2, 5)) # Potencia de base entera 
print("Potencia con módulo (2**5 % 3):", pow(2, 5, 3)) # Módulo de potencia de base entera

# b) Números decimales (float)
decimal = 3.1415
neg_decimal = -2.718
# Métodos de float
print("Fracción exacta:", decimal.as_integer_ratio()) # Fracción representativa del númerod decimal
print("¿Es entero?", decimal.is_integer()) # Comprobación de número entero (n.0)
print("Hexadecimal:", decimal.hex()) # Conversión a hexadecimal
print("Desde hexadecimal:", float.fromhex(decimal.hex())) # Conversión a decimal desde hexadecimal
# Funciones globales
print("Valor absoluto:", abs(neg_decimal)) # Eliminación del signo
print("Divmod (5.5, 2):", divmod(5.5, 2)) # División con cociente y resto
print("Potencia:", pow(decimal, 2)) # Potencia de base decimal
print("Redondeo entero más cercano:", round(decimal)) # Redondeo de un número decimal
print("Redondeo a 2 decimales:", round(decimal, 2)) # Redondeo de dos números decimales

# c) Números complejos (complex)
complejo = 2 + 3j
# Atributos
print("Parte real:", complejo.real) # Parte real
print("Parte imaginaria:", complejo.imag) # Parte imaginaria
# Método
print("Conjugado:", complejo.conjugate()) # Conjugado (Cambio de signo de parte imaginaria)
# Funciones globales
print("Magnitud:", abs(complejo)) # Eliminación del signo tras resolución
print("Potencia:", pow(complejo, 2)) # Potencia de base compleja

# d) Booleanos (bool)
verdadero = True
falso = False
# Comportamiento como números
print("True + True:", True + True) # Suma
print("False * 10:", False * 10) # Multiplicación



