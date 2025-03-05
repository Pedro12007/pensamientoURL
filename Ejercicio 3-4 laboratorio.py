#Ejercicio 1 
oracion = input("Ingresa una oración: ")
oracion = oracion.split()
print(f"Primera palabra: {oracion[0]}")
print(f"Ultima palabra: {oracion[(len(oracion)-1)]}")

#Ejercicio 2 
oracion = "Hola  mundo  en Python"
oracion = oracion.split()
print(" ".join(oracion))10:49 5/03/2025

#Ejercicio 3
correo = input("Ingrese un correo: ")
correo = correo.split("@")
print(correo[1])

#Ejercicio 4
doc = input("Ingrese el nombre de un documento pdf: ")
print(doc.endswith(".pdf"))

#Ejercicio 5
txt = input("Ingrese un texto: ")
txt = txt.split()
txt=txt[::-1]
txt = " ".join(txt)
print(txt)

#Ejercicio 6
clave = input("Ingrese una palabra clave: ")
poema_amor = """Dos claveles en el agua duran días y días,
pero mi amor por ti durará toda la vida.
Los claveles piden agua y los presos libertad
y yo pido que me quieras hasta la inmortalidad.
Dos claveles en el agua no se pueden marchitar,
dos personas que se quieren no se pueden olvidar."""

poema_triste = """Me miro triste las manos
después,
cuando escribo en medio
de la noche… (¡qué misterio!).
Me miro mi pobre mano,
estrella con cinco dedos,
estrella con cinco picos
estrella sin firmamento.
Y me parece mentira
que mi mano escriba versos."""

poema_alegre = """Alegre es la vida.
Y corta, pasajera.
Y es absurdo, 
y es antipático y zurdo
complicarla.
"""

poema_motivacion = """La motivación, llama que arde, guía tus pasos cuando todo es tarde. Es el susurro que rompe el miedo, la fuerza oculta tras cada ruedo.
No temas al reto, sigue adelante, con motivación, todo es constante.
"""

poema_naturaleza = """En la naturaleza yace el secreto, 
un mundo vasto, puro y discreto. 
Cantan las hojas al soplar el viento, 
y el río danza en su movimiento.
"""
if clave in poema_amor:
    print(poema_amor)
elif clave in poema_triste:
    print(poema_triste)
elif clave in poema_alegre:
    print(poema_alegre)
elif clave in poema_motivacion:
    print(poema_motivacion)
elif clave in poema_naturaleza:
    print(poema_naturaleza)
else: 
    print("La palabra no aparece en ningún poema.")