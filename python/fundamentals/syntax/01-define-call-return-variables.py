"""
Nivel 1: Lo Esencial (Definición y Llamada)

    El nacimiento: Define una función llamada iniciar_sistema que no reciba parámetros y retorne el string "Sistema iniciado".

    El despertar: Llama a la función iniciar_sistema que acabas de crear y guarda su resultado en una variable llamada estado.

    El mensajero local: Crea una función crear_perfil(nombre). Dentro de la función, crea una variable local llamada perfil_completo que una el nombre con el texto " - Usuario Registrado". Retorna esa variable local.

"""
print("==========  Nivel 1 ==========")

def iniciar_sistema ():
    return "Sistema iniciado"

print(iniciar_sistema())

print("==============================")

estado = iniciar_sistema()

print("==============================")

def crear_perfil(nombre):
    perfil_completo = nombre + " - Usuario Registrado"
    return perfil_completo

print(crear_perfil("Jean "))

print("==============================")

"""
Nivel 2: Print vs Return y Adiós Globales

    4. La trampa silenciosa: Crea una función calcular_doble(numero). Asegúrate de que retorne el doble del número matemático (y que no solo lo imprima en pantalla).

    5. Aislamiento (Backend seguro): Tienes una variable global tasa_iva = 0.19 declarada arriba de tu código. Crea una función calcular_total(precio, iva). Pásale el IVA como parámetro en lugar de leer la variable global desde adentro.

    6. Validación del vacío: Llama a una función inexistente o que no retorna nada usando la función integrada de Python print(). Por ejemplo, haz que una función solo tenga un print("hola") adentro, llámala y envuélvela en otro print(). Observa el None en tu terminal para que tu cerebro registre ese error visualmente.
"""

print("==========  Nivel 2 ==========")

def calcular_doble(numero):
    resultado = numero * 2
    return resultado

print(calcular_doble(8))

print("==============================")

tasa_iva = 0.19

def calcular_total(precio, iva):
    precio_total = precio + precio * iva
    return precio_total

print("==============================")

error = print("Hola")

print(print("Hola"))

print("==============================")

"""
Nivel 3: Condicionales Profesionales

    7. El booleano limpio: Crea una función verificar_stock(hay_disponibilidad). Si hay disponibilidad (usa el booleano limpio, sin == True), retorna "Producto en camino". Si no, retorna "Agotado".

    8. Lógica de negocio: Crea una función aplicar_penalidad(puntaje, tiene_infraccion). Si tiene infracción, reduce el puntaje a la mitad y retórnalo. Si no, retorna el puntaje intacto.
"""

print("==========  Nivel 3 ==========")

def verificar_stock(hay_disponibilidad):
    if hay_disponibilidad:
        return "Producto en camino"
    else:
        return "Agotado"
    
print("==============================")

def aplicar_penalidad(puntaje, tiene_infraccion):
    if tiene_infraccion:
        resultado_puntaje = puntaje / 2
        return resultado_puntaje
    else:
        return puntaje
    
print(aplicar_penalidad(10, True))
print(aplicar_penalidad(80, False))

print("==============================")

"""
Nivel 4: Composición (Data Analytics & Pipeline)

    9. El extractor (Función 1): Crea una función extraer_datos() que simule traer datos de una base de datos retornando el número 1000.

    10. El pipeline (Funciones 1 y 2): Crea otra función limpiar_datos(cantidad). Esta debe retornar la cantidad dividida entre 10. Ahora, usa el resultado de extraer_datos() como el parámetro exacto al momento de llamar a limpiar_datos().

"""

def extraer_datos():
    return 1000

def limpiar_datos(cantidad):
    resultado = cantidad / 10
    return resultado

resultado_final = limpiar_datos(extraer_datos())
print(resultado_final)
