"""
Module to illustrate ASSOCIATION between classes in Python.
"""

class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrar_info(self):
        print(f"Curso: {self.titulo}")


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = [] # Association with Curso (plural, as it is a list)

    def inscribirse(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"\nCursos inscritos por {self.nombre}:")
        if not self.cursos:
            print("No tiene cursos inscritos.")
        else:
            for curso in self.cursos:
                print(f"- {curso.titulo}")


# Main program
if __name__ == "__main__":
    # Course creation
    curso1 = Curso("Programacion orientada a objetos")
    curso2 = Curso("Base de datos")
    curso3 = Curso("Machine learning")

    # Student creation (instance with lowercase, Class with uppercase)
    estudiante1 = Estudiante("Carlos Gomez")

    # Enrollments
    estudiante1.inscribirse(curso1)
    estudiante1.inscribirse(curso2)
    estudiante1.inscribirse(curso3)

    # Show enrolled courses
    estudiante1.mostrar_cursos()