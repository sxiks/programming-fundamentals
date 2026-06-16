# Código para ilustrar la DEPENDENCIA entre clases.

class BaseDatos:
    # Molde para simular una base de datos
    def conectar(self):
        return "Conexión establecida con la base de datos"
        
    def obtener_datos(self):
        #Obtebemos los datos de la base de datos
        return ["Juan", "María", "Carlos"]


class Reporte:
    # Molde para crear reportes
    def generar_reporte(self, base_datos):
        print("Generando reporte...")
        
        print(base_datos.conectar())
        
        # Extrae la informacion de la base de datos
        datos = base_datos.obtener_datos()
        
        print("\nContenido del reporte:")
        for persona in datos:
            print(f"- {persona}")


# Programa principal
bd = BaseDatos()
reporte = Reporte()

# Creacion del reporte
reporte.generar_reporte(bd)