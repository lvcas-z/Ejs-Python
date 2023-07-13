class Perro:
    def __init__(self,nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        
    def ladrar(self):
        print(f"Woof woof {self.nombre}")
        
    def jugarConPelota(self):
        print(f"{self.nombre} esta jugando con una pelota")
            
    def __str__(self):
        return f"Nombre : {self.nombre} | Edad : {self.edad} | Raza : {self.raza}"
            
ovejero = Perro("Rami",7,"Ovejero Aleman")

print(ovejero)
ovejero.ladrar()
ovejero.jugarConPelota()