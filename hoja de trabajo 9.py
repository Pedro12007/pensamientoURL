#Ejercicio 1
def es_par_o_impar(n):
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

#Ejercicio 2
lista1 = [1,2,3,4,5]
def suma_lista(lista):
    n = 0
    for i in lista:
        n+=i
    return n
        
print(suma_lista(lista1))

#Ejercicio 3
def cuenta_regresiva(n):
    if n<0:
        print('¡Despegue!')
    else:
        print(n)
        cuenta_regresiva(n-1)
        
#Ejercicio 4
def cuenta_ascendente(n):
    if n<=0:
        return 0
    else:
        cuenta_ascendente(n-1)
        print(n)
        
#Ejercicio 5
def suma_hasta(n):
    if n==1:
        return 1
    else:
        return n + suma_hasta(n-1)

print(suma_hasta(4))

#Ejercicio 6
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

#Ejercicio 7
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        resto_minimo = minimo(lista[1:])
        if lista[0] < resto_minimo:
            return lista[0]
        else:
            return resto_minimo
        
#Juego
import time

def adivina_el_numero(numero, intentos, tiempo_inicio):
    if intentos == 0:
        print(f"Se acabaron tus intentos. El número secreto era {numero_secreto}.")
        return False

    intento_jugador = int(input(f"Ingresa un número: "))

    if intento_jugador == numero:
        tiempo_final = time.time()
        tiempo_total = round(tiempo_final - tiempo_inicio, 2)
        print(f"Adivinaste el número.")
        print(f"Te tomó {tiempo_total} segundos.")
        return True
    elif intento_jugador < numero:
        print(f"El número secreto es mayor que {intento_jugador}.")
    else:
        print(f"El número secreto es menor que {intento_jugador}.")

    return adivina_el_numero(numero, intentos - 1, tiempo_inicio)

numero_secreto = 80  
tiempo_inicial = time.time()
adivina_el_numero(numero_secreto, 5, tiempo_inicial)