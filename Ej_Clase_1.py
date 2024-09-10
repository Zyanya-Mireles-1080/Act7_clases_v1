print("Introduccion a clases")
class Animal:
    edad = 3
    raza="Chihuahua"
    comida = "Croquetas"
    def come(self):
        print("El perro come "+self.comida)

print(Animal)

print("Creando el objeto de la clase Animal")
perro = Animal()
print("La edad del perro es: ",perro.edad)
print("La raza del perro es ",perro.raza)
perro.come()