#Ejercicio 1
consumo = int(input("Ingrese el consumo en metros cubicos: "))
habitantes = int(input("Ingrese la cantidad de habitantes: "))

if consumo < 15:
    print(f"La tarifa es de Q{consumo*5}")

elif 15 <= consumo <= 30:
    if habitantes > 3:
        print(f"La tarifa es de Q{consumo*4}")
    elif habitantes == 3:
        print(f"La tarifa es de Q{consumo*4.5}")
    else:
        print(f"La tarifa son Q{consumo*5}")
elif consumo > 30:
    if habitantes > 5:
        print(f"La tarifa es de Q{consumo*3.5}")
    elif (habitantes%2)==0:
        print(f"La tarifa es de Q{consumo*4}")
    else:
        print(f"La tarifa es de Q{consumo*4.2}")
        
#Ejercicio 2
year = int(input("Ingrese el modelo del carro: "))
placa = input("Ingrese su placa: ")

if year >= 2001:
    if int(placa[len(placa)-1])%2 == 0:
        print("No circula los lunes.")
    elif int(placa[len(placa)-1])%2 != 0:
        print("No circula los viernes.")
    if year%2==0:
        print("No circula los sábados.")
else: 
    print("Advertencia: El carro necesita mantenimiento obligatorio.")