class Perro:
    # Esta funcion sirve para inizializar los atributos principales de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Mi perrito se llama {self.nombre}")

# Al llamar la clase perro se ejecuta el __init__ el cual es el que almacena los atributos principales de la clase

mi_perrito = Perro("Isis")
# Aqui por ultimo definimos el atributo "nombre" que definimos en la funcion __init__


class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Mi gatita se llama {self.nombre}")

mi_gato = Gato("Estrella")