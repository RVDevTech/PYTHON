# 1.3- Strings y sus métodos- 4. Otros tipo de modificaciones

# 1. str.maketrans() y translate()
texto = "abcdef"
mapa = str.maketrans("abc", "123", "f")# Creamos un mapa: 'a'→'1', 'b'→'2', 'c'→'3', eliminar 'f'
texto_modificado = texto.translate(mapa)

print("Original:", texto)
print("Modificado:", texto_modificado)


# 2. Escapes comunes

escapes = "Primera línea\nSegunda línea\tcon tabulación\\y comillas: \' \" \rSobreescribe inicio"
print("Escapes aplicados:")
print(escapes)

# 3. Escapes menos comunes
escapes_raros = "Retroceso\bFinal\fSalto de página\vTabulación vertical"
print("Escapes menos comunes:")
print(escapes_raros)

# 4. Raw strings
raw = r"Hola\nMundo\tTab\\Barra"
print("Raw string (no interpreta escapes):")
print(raw)

# 5. Función repr()
repr_cadena = repr("Hola\nMundo\tTab\\Barra") 
print("\nRepresentación oficial con repr():")
print(repr_cadena)

# La diferencia entre raw string y repr() es que repr() muestra las comillas




