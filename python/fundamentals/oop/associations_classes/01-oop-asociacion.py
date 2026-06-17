# Código para ilustrar la relación de ASOCIACIÓN entre clases.

class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrar_info(self):
        print(f"Curso: {self.titulo}")


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = [] # Asociación con Curso

    def inscribirse(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"\nCursos inscritos por {self.nombre}:")
        if not self.cursos:
            print("No tiene cursos inscritos.")
        else:
            for curso in self.cursos:
                print(f"- {curso.titulo}")


# Programa Principal
if __name__ == "__main__":
    # Creación de curso
    curso1 = Curso("Programacion orientada a objetos")
    curso2 = Curso("Base de datos")
    curso3 = Curso("Machine learning")

    # Creación de estudiante
    estudiante1 = Estudiante("Carlos Gomez")

    # Inscripciones
    estudiante1.inscribirse(curso1)
    estudiante1.inscribirse(curso2)
    estudiante1.inscribirse(curso3)

    # Mostrar cursos del estudiante
    estudiante1.mostrar_cursos()