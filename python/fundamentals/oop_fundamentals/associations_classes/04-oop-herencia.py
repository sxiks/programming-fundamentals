# Código para ilustrar la relación de HERENCIA entre clases.

class persona: # Molde padre con caracteristicas generales
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"email: {self.email}")

    
class Profesor(persona): # Molde hijo 1 el cual al poner "persona como parámetro" Hereda los datos del molde padre
    def __init__(self, nombre, email , especialidad):
        # Llamamos la el molde padre (persona), para que se encargue de guardar nombre y email, asi el molde hijo 1(Profesor) se encarga en guardar su especialidad
        super().__init__(nombre, email)
        self.especialidad = especialidad

    def impartir_clase(self):
        print(f"La profesora {self.nombre} \nEspecialidad: {self.especialidad} \nesta impartiendo.")


class Alumno(persona): # Molde hijo 2 el cual al poner "persona como parámetro" Hereda los datos del molde padre
    def __init__(self, nombre, email , codigo):
        # Llamamos la el molde padre (persona), para que se encargue de guardar nombre y email, asi el molde hijo 2(Alumno) se encarga en guardar su codigo
        super().__init__(nombre, email)
        self.codigo = codigo

    def estudiar(self):
        print(f"El alumno {self.nombre} \nCodigo: {self.codigo} \nesta estudiando.")


# Programa Principal
# Definimos los datos del Profesor
profesor_01 = Profesor(
    "Laura Torres",
    "laura@profesor.edu",
    "Física"
)

# Definimos los datos del Alumno
alumno_01 = Alumno(
    "Carlos Gomez",
    "carlos@alumno.edu",
    "A001"
)

# Imprimimos los datos del Profesor
print("\n=== DATOS DEL PROFESOR ===")
profesor_01.mostrar_informacion()
profesor_01.impartir_clase()

# Imprimimos los datos del Alumno
print("\n=== DATOS DEL ALUMNO ===")
alumno_01.mostrar_informacion()
alumno_01.estudiar()
