#Ejercicio 1
n = int(input('Tamaño array: '))
m = int(input('Multiplos: '))

salida = []

for i in range(1,n+1):
    salida.append(i*m)
print(salida)

#Ejercicio 2
tamaño = int(input("Ingrese la cantidad de nombres a ingresar: "))
nombres = []
largo = []
for i in range(tamaño):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    largo.append(len(nombre))
    
print(nombres)
print(largo)

#Escenario 1
n = int(input("Cantidad de clientes: "))

print("""Opciones:
5. Excelente
4. Muy Buena
3. Buena
2. Regular
1. Malo
""")

calificaciones = []
for i in range(n):
    calificacion = int(input("Ingrese su calificación del servicio: "))
    calificaciones.append(calificacion)

repeticion = []
for i in range(1,6):
    repeticion.append(calificaciones.count(i))

    
print("\nResultados: ")    
print(f"5. Excelente: {repeticion[4]}")
print(f"4. Muy buena: {repeticion[3]}")
print(f"3. Buena: {repeticion[2]}")
print(f"2. Regular: {repeticion[1]}")
print(f"1. Malo: {repeticion[0]}")

print(f"\nMás frecuente: {repeticion.index(max(repeticion))+1}")

