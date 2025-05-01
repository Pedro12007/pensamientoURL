# Ejercicio 1
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def datos(self):
        print(f'Su nombre es {self.nombre}. Tiene {self.edad} años. Pesa {self.peso} kg.')
        
    def dosis(self):
        print(f'La dosis de {self.nombre} es: ')
        
    def ficha_medica(self):
        print('Ficha médica')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad} años.')
        print(f'Peso: {self.peso} kg.')

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza
        
    def datos(self):
        super().datos()
        print(f'Su raza es {self.raza}.')
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*10} mg')
        
    def ficha_medica(self):
        super().ficha_medica()
        print(f'Raza: {self.raza}')
        
class Gato(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza
        
    def datos(self):
        super().datos()
        print(f'Su raza es {self.raza}.')  
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*5} mg')

    def ficha_medica(self):
        super().ficha_medica()
        print(f'Raza: {self.raza}')    

class Ave(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie
        
    def datos(self):
        super().datos()
        print(f'Su especie es {self.especie}.')
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*4} mg')

    def ficha_medica(self):
        super().ficha_medica()
        print(f'Especie: {self.especie}')

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color
        
    def datos(self):
        super().datos()
        print(f'Su color es {self.color}.')
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*11} mg')

    def ficha_medica(self):
        super().ficha_medica()
        print(f'Color: {self.color}')

perro = Perro('Mateo', 10, 15, 'Shi tzu')
gato = Gato('Tiger', 8, 5, 'Siamés')
ave = Ave('Cabo', 10, 100, 'Pinguino')
reptil = Reptil('Snake', 2, 3, 'Café')

perro.datos()
print()
gato.dosis()
print()
ave.ficha_medica()
print()
reptil.ficha_medica()
print()

#Ejercicio 2
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def info(self):
        print('Información personal:')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad} años')
        print(f'DNI: {self.dni}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carnet, grado, promedio):
        super().__init__(nombre, edad, dni)
        self.carnet = carnet
        self.grado = grado
        self.promedio = promedio

    def info(self):
        super().info()
        print(f'Carnet: {self.carnet}')
        print(f'Grado: {self.grado}')
        print(f'Promedio: {self.promedio}')

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, id_empleado, curso):
        super().__init__(nombre, edad, dni)
        self.id_empleado = id_empleado
        self.curso = curso

    def info(self):
        super().info()
        print(f'ID de empleado: {self.id_empleado}')
        print(f'Curso impartido: {self.curso}')

class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, id_empleado, puesto):
        super().__init__(nombre, edad, dni)
        self.id_empleado = id_empleado
        self.puesto = puesto

    def info(self):
        super().info()
        print(f'ID de empleado: {self.id_empleado}')
        print(f'Puesto: {self.puesto}')


est1 = Estudiante('Juan', 15, 123456789, '1505625', 'Quinto Bachillerato', 93)
cat1 = Profesor('Carlos', 30, 213546789, 12345, 'Matemática')
adm1 = Administrativo('Luis', 40, 987654321, 56789, 'Secretario')
est1.info()
print()
cat1.info()
print()
adm1.info()