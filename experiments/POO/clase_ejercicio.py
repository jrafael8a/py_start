class Coche:
    def __init__(self, brand, model, km=0):
        self.marca = brand
        self.modelo = model
        self.kilometraje = km

    def conducir(self, km):
        self.kilometraje += km
        print("Has conducido", km, "km. Kilometraje total:", self.kilometraje, "km.")


mi_coche = Coche("Toyota", "Corola")
mi_coche.conducir(50)
mi_coche.conducir(100)
