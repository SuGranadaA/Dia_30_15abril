#Importamos la librería para expresiones regurales
import re

#Creamos una frase
ejemplo1 = "Si quieres algo que nunca has tenido tendrás que hacer algo que nunca has hecho, If you want something that you have never had you will have to do something you have never done"
print("\nLa frase para el primer ejercicio es: \n", ejemplo1, "\n")

#Buscamos la palabra -algo- en la frase
op1 = re.search("algo", ejemplo1)

#Identificamos si la palabra -algo- está en la frase
if op1:  #Si está, se imprime el mensaje a continuación y el resultado
    print("\nSe encontró la palabra -algo- en la frase: \n", op1, "\n")
else:  #De lo contrario, se imprime el mensaje a continuación
    print("\nNo se encontró la palabra -algo- en la frase\n")

#Identificamos la posición en la cual comienza la coinciencia
print(
    "\nPosición en la que comienza la coincidencia de la palabra -algo- en la frase: \n",
    op1.start(), "\n")

#Identificamos la posición en la cual finaliza la coincidencia
print(
    "\nPosición en la que fializa la coincidencia de la palabra -algo- en la frase : \n",
    op1.end(), "\n")

#Identificamos y creamos una tupla con las posiciones en las cuales comienza y finaliza la coincidencia
print(
    "\nPosiciones en las cuales comienza y finaliza la coincidencia de la palabra -algo- en la frase: \n",
    op1.span(), "\n")

#Identificamos si la palabra -quieres- se encuentra al comienzo de la cadena
op2 = re.match("quieres", ejemplo1)

#Identificamos si la palabra está al comienzo de la frase
if op2:  #Si está, se imprime el mensaje a continuación y el resultado
    print("\nSe encontró la palabra -quieres- al comienzo de la frase: \n",
          op2, "\n")
else:  #De lo contrario, se imprime el mensaje a continuación
    print("\nNo se econtró la palabra -quieres- al comienzo de la frase\n")

#Identificamos donde hay un -go- para dividir la frase
op3 = re.split("go", ejemplo1)

#Identificamos si hay un -go- para dividir la frase
if op3:  #Si está, se imprime el mensaje a continuación y el resultado
    print("\nSe dividió la cadena cada que se encntró un -go- en la frase: \n",
          op3, "\n")
else:  #De lo contrario, se imprime el mensaje a continuación
    print(
        "\nNo se dividió la cadena al no encontrar al menos un -go- en la frase\n"
    )

#Identificamos los dos primeros cortes que se hicieron con -go-
op4 = re.split("go", ejemplo1, maxsplit=2)

#Imprimimos el resultado
print(
    "\nSe dividió la cadena cada vez al encontrar un -go- y a continuación, las dos primeras partes: \n",
    op4, "\n")

#Identificamos las coincidencias de la palabra -que- en la frase
op5 = re.findall("que", ejemplo1)

#Idetificamos si hay coincidencias de la palabra -que- en la frase
if op5:  #Si está, se imprime el mensaje a continuación y el resultado
    print("\nLista con las coincidencias de la palabra -que- en la frase: \n",
          op5, "\n")
else:  #De lo contrario, se imprime el mensaje a continuación
    print("\nNo se encontraron coincidencias de la palabra -que-")

#Sustituimos la palabra -has- por -hayas- en la frase
op6 = re.sub("has", "hayas", ejemplo1)

#Identificamos si es posible susstituir la palabra -has- por -hayas- en la frase
if op6:  #Si es posible, se imprime el mensaje a continuación y el resultado
    print(
        "\nSe reemplazó la palabra -has- por la palabra -hayas- en la frase y quedó así: \n",
        op6, "\n")
else:  #De lo contrario, se imprime el mensaje a continuación
    print(
        "\nNo se encontraron coincidencias de la palabra -has- para hacer el reemplazo\n"
    )

#Identificamos 2 patrones con valores distintos para el ejercicio
op7 = re.findall("Si|If", ejemplo1)

#Imprimimos el resultado
print("\nDos patrones con valores distintos: \n", op7, "\n")

#Creamos la frase para el ejercicio
ejemplo2 = "Cuando era pequeña, pronunciaba mi animal favorito como vca , luego aprendí a decirle vaca ; cuando estaba lejos y quería que viniera, la llamaba vaaca ; una vez que se pedió, la llamé vaaaca , hasta que luego de muchos años un día se nos fue y en mis sueños solo llamaba vaaaaaca"
print("\nLa frase para el siguiente ejercicio es: \n", ejemplo2, "\n")

#Definimos ninguna o más repeticiones de la letra a la izquierda del *
op8 = re.findall(r'va*', ejemplo2)
print("\nMétodo con *: \n", op8, "\n")

#Definimos una o más repeticiones de la letra a la izquierda de +
op9 = re.findall(r'va+', ejemplo2)
print("\nMétodo con +: \n", op9, "\n")

#Definimos una o ninguna repetición de la letra a la izquerda de ?
op10 = re.findall(r'va?', ejemplo2)
print("\nMétodo con ?: \n", op10, "\n")

#Creamos la frase para el ejercicio
ejemplo3 = "sabado s4b4d0"
print("\nLa frase para el siguiente ejercicio es: \n", ejemplo3, "\n")

#Definimos un rango con caracteres alfabéticos
op11 = re.findall("s[a-z]bado", ejemplo3)
print("\nCon rango alfabético: \n", op11, "\n")

#Definimos un rango con caracteres numéricos
op12 = re.findall("s[0-9]b[0-9]d[0-9]", ejemplo3)
print("\nCon rango numérico: \n", op12, "\n")

#Creamos la frase para el ejercicio
ejemplo4 = "Desde pequeña he ahorrado para una casa , y hasta ahora tengo 55000 pesos ; me faltan 7500 para comprar mi casa de muñecas"
print("\nLa frase para el siguiente ejercicio es: \n", ejemplo4, "\n")

#Identificamos los caracteres numéricos
op13 = re.findall(r"\d+", ejemplo4)
print("\nLos caracteres numéricos son: \n", op13, "\n")

#Identificamos los caracteres alfabéticos
op14 = re.findall(r"\D+", ejemplo4)
print("\nLos carateres alfabéticos son: \n", op14, "\n")

#Identificamos los espacios en blanco de la frase
op15 = re.findall(r"\s+", ejemplo4)
print("\nLos espacios en blanco que contiene la frase son: \n", op15, "\n")

#Identificamos los caracteres diferentes a espacio en blanco
op16 = re.findall(r"\S+", ejemplo4)
print("\nLos caracteres que no son espacio en blanco son: \n", op16, "\n")

#Identificamos los caracteres alfanuméricos
op17 = re.findall(r"\w+", ejemplo4)
print("\nLos caracteres alfanuméricos son: \n", op17, "\n")

#Identificamos los caracteres o alfanuméricos
op18 = re.findall(r"\W+", ejemplo4)
print("\nLos caracteres no alfanuméricos son: \n", op18, "\n")
