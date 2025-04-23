#Ejercicio 1
def es_par_o_impar(n):
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

#Ejercicio 2
lista = [1,2,3,4,5]
def suma_lista(lista):
    n = 0
    for i in lista:
        n+=i
    return n
        
print(suma_lista(lista))

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
