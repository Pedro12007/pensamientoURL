#Tarea 6 laboratorio

saldo = 3000
error = 0

while saldo > 0 and error < 3:
	dinero = int(input("Ingrese la cantidad de dinero a retirar: "))
	if dinero <= saldo:
		saldo -= dinero
		if saldo > 0:
			print(f"Retiro exitoso. Nuevo saldo: Q{saldo}")
		if saldo == 0:
			print("Retiro exitoso. Saldo agotado. Adiós.")
			break
	else:
		error += 1
		print(f"Saldo insuficiente. Intentos restantes: {3-error}")