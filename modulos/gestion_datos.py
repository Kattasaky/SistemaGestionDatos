# Módulo para gestionar almacenamiento de datos en archivo.

def guardar_datos(nombre, edad):
    # Guardar datos en un archivo de texto
    with open("datos.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre},{edad}\n")
    print("✅ Datos guardados en archivo.")

def listar_datos():
    try:
        with open("datos.txt", "r", encoding="utf-8") as f:
            print("\n=== Lista de datos registrados ===")
            for linea in f:
                nombre, edad = linea.strip().split(",")
                print(f"Nombre: {nombre}, Edad: {edad}")
    except FileNotFoundError:
        print("No hay datos registrados.")

