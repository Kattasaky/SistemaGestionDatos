# Módulo para gestionar almacenamiento de datos.

# Lista general para guardar los registros
datos_guardados = []

def guardar_datos(nombre, edad):
    datos_guardados.append({"nombre": nombre, "edad": edad})
    print("✅ Datos guardados correctamente.")

def listar_datos():
    if not datos_guardados:
        print("No hay datos registrados.")
    else:
        print("\n=== Lista de datos registrados ===")
        for persona in datos_guardados:
            print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
