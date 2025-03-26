#Ejercicio 1
for i in range(11):
    if i % 2 != 0:
        print(i)
        
#Ejercicio 2
contador = 0
while contador < 11:
    if contador % 2 != 0:
        print(contador)
    contador += 1    
    
#Escenario 1
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "chupacabra":
        print("¡Has dejado el bucle con éxito")
        break
    
#Escenario 2
user_word = input("Ingrese una palabra: ").upper()

for i in user_word:
    if i in "AEIOU":
        continue
    else:
        print(i)
