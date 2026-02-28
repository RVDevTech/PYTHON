# PYTHON: PROGRAMACIÓN BACKEND Y TRATAMIENTO DE DATOS

![alt text](ASSETS/image.png)

## -ÍNDICE:
### A) Tratamiento de datos básicos y estructuras lógicas:
- **0- Introducción.**
- **1- Sintaxis y fundamentos del lenguaje:**
  * 1.1- Asignación de variables y tipos de datos primitivos 
  * 1.2- Impresión de datos y variables 
  * 1.3- Strings y sus métodos 
## A) Tratamiento de datos básicos y estructuras lógicas:

### 0- Introducción:
 * #### ¿Qué es Python?
<p align="justify">
 <strong>Python</strong> es un lenguaje de programación<strong> versátil, moderno y fácil de aprender,</strong> ampliamente utilizado en desarrollo web, ciencia de datos, inteligencia artificial, automatización y mucho más. Su sintaxis clara y legible lo hace <strong> ideal tanto para principiantes como para desarrolladores experimentados, </strong> permitiendo escribir código eficiente y mantenible.
</p>

![alt text](ASSETS/Python-logo.png)

* #### ¿Para qué sirve y por qué es importante?

<strong>Python</strong> se ha convertido en uno de los lenguajes más importantes del mundo tecnológico por varias razones:<br>
<br><strong> - Multipropósito</strong>: permite crear desde aplicaciones web hasta  <strong>sistemas de inteligencia artificial.</strong>  <br>
<strong>- Gran comunidad y ecosistema</strong>: bibliotecas como  <strong>NumPy, Pandas, FastAPI o TensorFlow </strong>facilitan el desarrollo de soluciones complejas.  <br>
<strong>- Lectura y mantenimiento fácil</strong>: la sintaxis clara reduce errores y acelera el aprendizaje.  <br>
- <strong>Popularidad y demanda laboral</strong>: es el <strong>lenguaje preferido en startups</strong>, empresas tecnológicas y proyectos de investigación.  

---
* #### Sobre este repositorio:
<p align="justify">
 Este repositorio contiene <strong>apuntes didácticos de Python</strong>, diseñados para aprender paso a paso de manera visual y práctica. Está organizado en dos secciones principales:<br>
 <br><strong>1. Cuaderno de apuntes:</strong> <br>
   - Explica la teoría de <strong>Python de manera estructurada.</strong>  <br>
   - Incluye <strong>ejemplos de código</strong> que ilustran los conceptos aprendidos. <br> 
 <br><strong>2. Carpeta de Programas (Ejercicios prácticos):</strong> <br>
   - Contiene <strong>ejercicios reales</strong> que permiten experimentar con el código.  <br>
   - Cada ejemplo refleja <strong>situaciones prácticas </strong>y ayuda a reforzar los conocimientos adquiridos en los apuntes teóricos.  <br>
 <br>Este enfoque permite <strong>aprender teoría y práctica simultáneamente,</strong> facilitando la comprensión y memorización de <strong>Python</strong> de forma visual y aplicada.
</p>

![alt text](ASSETS/visual-studio-code-banner-image.jpg)

* #### Sobre la instalación y uso del editor de código:

<p align="justify">
Para poder programar en <strong>Python</strong> es necesario utilizar un <strong>editor de código,</strong> que es una herramienta que nos permite <strong>escribir, organizar y ejecutar nuestro código</strong> de manera más cómoda y visual que un simple bloc de notas. Un buen editor ayuda a <strong>detectar errores, resaltar la sintaxis y ejecutar programas de forma directa.</strong>
</p>

<p align="justify">
En este repositorio, todo el trabajo se ha realizado utilizando <strong>Visual Studio Code (VS Code),</strong> que es un editor <strong>gratuito, ligero y muy popular</strong> entre programadores de todos los niveles. <strong>VS Code</strong> permite <strong>abrir archivos de Python, organizar carpetas de proyectos, ejecutar scripts y ver resultados directamente dentro del editor.</strong>
</p>

<p align="justify">
Para <strong>empezar a usar Python con VS Code,</strong> los pasos básicos son los siguientes:<br><br>
<strong>1.</strong> Instalar <strong>Python</strong> desde su página oficial (<a href="https://www.python.org/">python.org</a>). Asegúrate de marcar la opción <strong><em>"Add Python to PATH"</em></strong> durante la instalación.<br>
<strong>2.</strong> Descargar e instalar <strong>VS Code</strong> desde su sitio oficial (<a href="https://code.visualstudio.com/">code.visualstudio.com</a>), que es gratuito.<br>
<strong>3.</strong> Abrir <strong>VS Code y añadir la extensión oficial de Python</strong> para que el editor reconozca los archivos <strong>.py</strong> y permita ejecutar scripts fácilmente.<br>
<strong>4.</strong> Crear un proyecto o abrir una carpeta donde guardar tus archivos de <strong>Python</strong>.<br>
<strong>5.</strong> Escribir tu primer script, por ejemplo, <strong>print("¡Hola mundo!"),</strong> y ejecutarlo usando la <strong>terminal integrada del editor.</strong>
</p>

<p align="justify">
Con este enfoque, incluso <strong>los más principiantes pueden empezar a programar sin complicaciones,</strong> siguiendo los ejemplos y ejercicios que se incluyen en este repositorio. Así, aprender <strong>Python</strong> se vuelve <strong>visual, práctico y ordenado,</strong> aprovechando al máximo las herramientas de <strong>VS Code</strong>.
</p>

---
### 1- Sintaxis y fundamentos del lenguaje:

* #### 1.1- Asignación de variables  y tipos de datos primitivos:

En **Python existen diferentes tipos de datos básicos:**<br>
•	**Strings (str):** cadenas de texto (P.ej.: ”Hola, María”).<br>
•	**Números enteros (int):** números de tipo entero (P.ej.: 3, -5).<br>
•	**Números decimales (float):** números de tipo decimal (P.ej.: 2.1, -0.5).<br>
•	**Números complejos (complex):** números de tipo complejo (P.ej.: 2+3j).<br>
•	**Booleanos(bool):** valores lógicos que toman valores del tipo **(True/False).**<br>
<p align="justify">
   <strong>Python es de tipado dinámico,</strong> lo que significa que <strong>no se declara el tipo explícitamente;</strong> el intérprete <strong>lo deduce automáticamente.</strong><br>
   Para <strong>asignar un valor de cualquier tipo a una variable,</strong> debemos usar el <strong>operador de asignación “=”.</strong>
</p>

![alt text](<ASSETS/Captura de pantalla 2026-02-27 074025.png>)<br>
Si queremos conocer **el tipo de dato** de una variable o valor, usamos **type ():**<br>

![alt text](<ASSETS/Captura de pantalla 2026-02-27 075624.png>)

* #### 1.2- Impresión de datos y variables:

<p align="justify">
   Para <strong>imprimir una variable</strong> o dato en <strong>Python</strong> se utiliza la función <strong>print().</strong> Para imprimir varias de ellas, se deben <strong>separar por comas dentro de ().</strong> No obstante, estas variables pueden <strong>mostrarse de distintas formas al imprimirse</strong> y su presentación puede configurarse mediante <strong>argumentos de la función:</strong>
</p>

* **Parámetros modificables:** 

![alt text](<ASSETS/Captura de pantalla 2026-02-27 085856.png>)

•	***Objects:** los objetos que se pasan como **argumentos variables.**
<p align="justify">
   •	<strong>Sep:</strong> separación entre <strong>elementos de diferentes variables o una misma cadena de texto</strong>. Por defecto, <strong>toma el valor de “ ”</strong> (Espacio). 
</p>

-	<strong>Modificable para tomar otros valores</strong> tales como <strong>“-“,</strong> <strong>“”</strong> (Nada), <strong>“\n”</strong> (Salto de línea) o <strong>“\t”</strong> (<strong>Tabulación=</strong> 4/8 espacios visuales).

<p align="justify">
   •<strong> End:</strong> separación <strong>del final de la variable o una cadena de texto </strong>respecto a la siguiente orden.. Por defecto, <strong>toma el valor “\n”.</strong>
</p>

-    <strong>Modificable para tomar otros valores</strong> tales como <strong>“-“,</strong><strong> “ ”,</strong> <strong>“”</strong> o <strong>“\t”.</strong>
<p align="justify">
   •<strong> File:</strong> elige la <strong>terminal o documento de salida del dato o variable </strong>pudiendo ejecutarse en <strong>la terminal del editor de código </strong>(asignación por defecto),<strong> la terminal de errores </strong>u<strong> otro documento del tipo .txt. .</strong>Por defecto, <strong>toma el valor “\n”.</strong>
</p>

-	**Salida en la terminal:** sys.stdout
-	**Salida en el flujo de error estándar:** sys.stderr
-	Para usarlo explícitamente **hay que importarlo** (Explicado más adelante)

<p align="justify">
   •<strong> Flush:</strong> elige si<strong> forzar la escritura de un dato o variable de manera inmediata </strong>o si <strong>almacenarlo en el búfer junto con el resto de órdenes.</strong>
</p>
 
-	**Salida inmediata:** True
-	**Almacenamiento en el búfer:** False (valor por defecto)
<br>

<p align="justify">
   Por otra parte, cuando escribimos código en <strong>Python,</strong> es recomendable acompañarlo de <strong> comentarios y docstrings </strong> para facilitar su comprensión:
</p>
 
- **Tipos de comentarios:**
  * **Comentarios de una sola línea,** que se indican con el **símbolo #.**
  * **Comentarios de varias líneas / docstrings:**
    *	Se usan **triples comillas """ ... """** para **abrir y cerrar el comentario** en varias líneas.
    *	Más adelante veremos que, **al usarlos para definir funciones,** se pueden **consultar desde el código mediante el atributo** .__doc_ _.

![alt text](<ASSETS/Captura de pantalla 2026-02-27 090046.png>)

![alt text](<ASSETS/Captura de pantalla 2026-02-27 090150.png>)

* #### 1.3- Strings y sus métodos:

<p align="justify">
   Los strings <strong>son inmutables.</strong> Sus métodos <strong>no modifican la cadena original,</strong> sino que devuelven <strong>una nueva.</strong>
</p>

* #### 	Métodos (str.metodo() ):

**- Métodos de formato y transformación:**

 •	**.lower ():** convierte todo el **texto a minúsculas.**<br>
 •	**.upper ():** convierte todo el **texto a mayúsculas.**<br>
 •	**.title ():** pone en **mayúscula la primera letra de cada palabra.**<br>
 •	**.capitalize ():** pone en **mayúscula la primera letra de la cadena completa.**<br>
 •	**.swapcase ():** invierte las **mayúsculas y minúsculas.**<br>
 •	**.casefold ():** aplana **cualquier tipo de caracteres a minúsculas** (Más agresivo).<br>
 •	**.strip (chars=None):** elimina **espacios o caracteres** indicados al **inicio y final.**<br>
 •	**.lstrip (chars=None):** elimina **espacios o caracteres** indicados solo **en el inicio.**<br>
 •	**.rstrip (chars=None):** elimina **espacios o caracteres** indicados solo **en el final.**<br>
 •	**.ljust (width, fillchar=' '):** **alinea el texto a la izquierda** rellenando hasta width con fillchar.<br>
 •	**.rjust (width, fillchar=' '):** alinea el texto a la derecha rellenando hasta **width** con **fillchar.**<br>
 •	**.center (width, fillchar=' '):** **centra el texto** en **width** rellenando con **fillchar.**<br>
 •	**.zfill (width):** rellena con **ceros a la izquierda hasta width.**<br>
 •	**.replace (old, new, count=-1 o count=n):** **sustituye texto por otro** (opcional limitar cantidad con **“n”**, de lo contrario **será -1 por defecto**)<br>
 •	**.removeprefix (prefix):** **elimina un prefijo** exacto si existe.<br>
 •	**.removesuffix (suffix):** **elimina un sufijo** exacto si existe.<br>
 •	**.expandtabs (tabsize=n):** sustituye **“\t” por “n” espacios** según tamaño de tabulación.

![alt text](<ASSETS/Captura de pantalla 2026-02-28 142443.png>)

![alt text](<ASSETS/Captura de pantalla 2026-02-28 144005.png>)


**- Métodos de búsqueda y separación:**

 •	**.find (sub):** busca la **primera aparición** de la subcadena **sub** y devuelve **su índice**, o **-1 si no existe.**<br>
 •	**.rfind (sub):** busca la **última aparición** de la subcadena **sub** y devuelve **su índice**, o **-1 si no existe.**<br>
 •	**.count (sub):**   cuenta **cuántas veces** aparece la subcadena **sub.**<br>
 •	**.index (sub):** igual que **.find (),** devuelve el **índice de la primera aparición de sub**, pero si no lo encuentra lanza un **ValueError,** que **frenará el código** a menos que le asignemos una **acción alternativa.**<br>
 •	**.partition (sep):** divide la cadena en **tres partes** usando la **primera aparición del separador sep,** creando una **tupla** (que veremos más adelante).<br>
 •	**.rpartition ():** divide la cadena en **tres partes** usando la **última aparición del separador sep,** creando una **tupla.**<br>
 •	**slicing [start:stop:step]:** extrae **subcadenas de la cadena usando índices,** contando el de **inicio pero no el de final,** y con distancia **step** (Por defecto 1).

Cada **letra o carácter en una cadena de texto tiene un índice,** que nos permite acceder a él usando **corchetes [ ].** Los índices pueden ser **positivos o negativos,** y esto determina **desde dónde contamos:**

![alt text](<ASSETS/Captura de pantalla 2026-02-28 144016.png>)

<p align="justify">
   Los <strong>índices positivos</strong> comienzan en <strong>0 desde el primer carácter</strong> y aumentan de <strong>izquierda a derecha</strong> (P.ej.: en la palabra "Python" la 'P' tiene índice 0, la 'y' índice 1 y así sucesivamente hasta la 'n' que tiene índice 5).
</p>
<p align="justify">
   Por otro lado, los <strong>índices negativos</strong> comienzan en <strong>-1 desde el último carácter</strong> y disminuyen de <strong>derecha a izquierda</strong> (P.ej.: en el mismo ejemplo, la 'n' tiene índice -1, la 'o' índice -2 y la 'P' índice -6).
</p>

![alt text](<ASSETS/Captura de pantalla 2026-02-28 155318.png>)
![alt text](<ASSETS/Captura de pantalla 2026-02-28 160343.png>)

**- Métodos de comprobación booleana:**

 •	**.isalpha():** devuelve <strong><em>True</em></strong> si todos **los caracteres son letras** y hay al menos uno.<br>
 •	**.isdigit():** devuelve <strong><em>True</em></strong> si todos **los caracteres son dígitos numéricos.**<br>
 •	**.isdecimal():** devuelve <strong><em>True</em></strong> si todos **los caracteres son dígitos numéricos** en **formato estándar** y pertenecientes a **0-9.**<br>
 •	**.isnumeric():** devuelve <strong><em>True</em></strong> si **los caracteres son números** (P.ej.: IV, 4).<br>
 •	**.isalnum():** devuelve <strong><em>True</em></strong> si solo hay **letras o números.**<br>
 •	**.isprintable():** devuelve <strong><em>True</em></strong> si todos **los caracteres se pueden imprimir** (no contiene saltos de línea, tabulaciones, etc.).<br>
 •	**.isspace():** devuelve <strong><em>True</em></strong> si la cadena contiene **solo espacios,** **\t** o **\n.**<br>
 •	**.isascii():** devuelve <strong><em>True</em></strong> si los **caracteres son ASCII** **(códigos 0–127).**<br>
 •	**.islower():** devuelve <strong><em>True</em></strong> si todas **las letras están en minúscula.**<br>
 •	**.isupper():** devuelve <strong><em>True</em></strong> si todas **las letras están en mayúscula.**<br>
 •	**.istitle():** devuelve <strong><em>True</em></strong> si la cadena está formada por títulos.<br><br>
 •	**.isidentifier():** devuelve <strong><em>True</em></strong> si el **nombre de variable es válido.**<br>
 •	**.startswith(prefijo):** devuelve <strong><em>True</em></strong> si la **cadena empieza por el prefijo.**<br>
 •	**.endswith(sufijo):** devuelve <strong><em>True</em></strong> si la **cadena termina por el sufijo.**

![alt text](<ASSETS/Captura de pantalla 2026-02-28 162640.png>)
![alt text](<ASSETS/Captura de pantalla 2026-02-28 162808.png>)