matriz= [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]

def siguiente_generacion(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1: 
                if (i == 0 and j == 0):
                    pass
            


#3. Buscar un número en la matriz
buscar = int(input("Buscar el numero:  "))
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == buscar:
            print(f"Número encontrado en posición [{i}][{j}]")
            encontrado = True

if not encontrado:
    print("Número no encontrado.")


#4. Eliminar un número de la matriz (reemplazar por 0)
eliminar = int(input("¿Qué número quieres eliminar (reemplazar por 0)? "))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == eliminar:
            matriz[i][j] = 0

print("Matriz después de eliminar:")
for fila in matriz:
    print(fila)


        
print(siguiente_generacion(matriz))
