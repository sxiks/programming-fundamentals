# Código para ilustrar la relación de HERENCIA entre clases.

class persona:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.nombre = email

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"email: {self.email}")

    
class Profesor(persona):
    def __init__(self, nombre, email , especialidad):
        super().__init__(nombre, email)
        self.especialidad = especialidad

    def impartir_clase(self):
        print(f"El profesor {self.nombre} esta impartiendo")


class Alumno(persona):
    def __init__(self, nombre, email , codigo):
        super().__init__(nombre, email)
        self.codigo = codigo

    def estudiar(self):
        print(f"El alumno {self.nombre} esta estudiando.")

    
# Programa Principal

Profesor = Profesor(
    "Laura Torres",
    "carlos@estudiante.edu",
    "A001"
)

Alumno = Alumno (
    "Carlos Gomez",
    "carlos@estudiate.edu",
    "A001"
)

print("\n=== DATOS DEL PROFESOR ===")
Profesor.mostrar_informacion()
Profesor.impartir_clase()

print("\n=== DATOS DEL ALUMNO ===")
Alumno.mostrar_informacion()
Alumno.estudiar()
