class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def datos(self):
        print(f'Su nombre es {self.nombre}. Tiene {self.edad} años. Pesa {self.peso} kg.')
        
    def dosis(self):
        print('La dosis es: ')
        
    def ficha_medica(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Peso: {self.peso}')

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza
        
    def datos(self):
        super().datos()
        print(f'Su raza es {self.raza}')
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*10} mg')
        
        
class Gato(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza
        
    def datos(self):
        super().datos()
        print(f'Su raza es {self.raza}')  
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*5} mg')

class Ave(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie
        
    def datos(self):
        super().datos()
        print(f'Su especie es {self.especie}')
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*4} mg')

class Reptil(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.color = color
        
    def datos(self):
        super().datos()
        print(f'Su color es {self.color}')
        
    def dosis(self):
        super().dosis()
        print(f'{self.peso*11} mg')

perro = Perro('Mateo', 15, 100, 'shi tzu')
perro.datos()
perro.dosis()
