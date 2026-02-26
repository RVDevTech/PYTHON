# 1.2- Impresión de datos y variables 
#Esto es un comentario de una línea
"""
Esto es un comentario multilínea
de extensión variable
"""
import sys # Importamos sys para poder llevar a cabo el ejemplo, que más adelante explicaremos

valor1 = "Hola"
valor2 = 123
valor3 = True

# *objects: imprime los valores
print(valor1, valor2, valor3)

# sep: separación entre valores
print(valor1, valor2, valor3, sep="-")   # Separador con guion
print(valor1, valor2, valor3, sep="")    # Sin separación
print(valor1, valor2, valor3, sep="\n")  # Separador con salto de línea
print(valor1, valor2, valor3, sep="\t")  # Separador con tabulación

# end: qué se imprime al final
print(valor1, end="-")    # Termina con guion
print(valor1, end=" ")    # Termina con espacio
print(valor1, end="")     # Termina sin separación
print(valor1, end="\t")   # Termina con tabulación 

# file: impresión en la terminal habitual (sys.stdout)
# Salida en la terminal habitual
print("Este texto va a sys.stdout", file=sys.stdout)

# flush: fuerza escritura inmediata
print("Texto con flush=True", flush=True) # Se escribe inmediatamente
print("Texto con flush=False")            # Se almacena en el buffer 





