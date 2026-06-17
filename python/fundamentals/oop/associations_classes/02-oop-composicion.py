# Código para ilustrar la relación de COMPOSICIÓN entre clases.

class Aula: # Molde para Aulas
    # Al crearse se exige el codigo y capacidad
    def __init__(self, codigo, capacidad):
        self.codigo = codigo
        self.capacidad = capacidad
        print(f"Aula {self.codigo} creada.")

    def mostrar_info(self):
        print(f"Aula: {self.codigo} - Capacidad: {self.capacidad}")

    def __del__(self):
        print(f"Aula {self.codigo} eliminada.")


class Escuela: # Molde para Escuela
    # Al nacer se exige el nombre
    def __init__(self, nombre):
        self.nombre = nombre

        # La escuela crea sus propias aulas
        self.aulas = [
            Aula("A101", 30),
            Aula("A102", 25),
            Aula("LAB01", 20)
        ]
        
        print(f"Escuela {self.nombre} creada.")

    def mostrar_aulas(self):
        print(f"\nEscuela: {self.nombre}")

        for aula in self.aulas:
            aula.mostrar_info()

    def __del__(self):
        print(f"\nEscuela {self.nombre} eliminada.")


# Programa Principal
if __name__ == "__main__":
    # Creacion de la escuela
    escuela_01 = Escuela("SENA")
    
    # Mostrar aulas
    escuela_01.mostrar_aulas()