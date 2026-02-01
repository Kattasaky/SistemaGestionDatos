# Este es el punto de entrada del sistema de gestión de datos.
# Aquí se coordinan los módulos y se ejecuta el flujo principal.

from modulos import menu, datos_basicos, validaciones, gestion_datos

def main():
    print("=== Sistema de Gestión de Datos ===")

    # Mostrar menú principal
    opcion = menu.mostrar_opciones()

    if opcion == "1":
        # Pedir datos básicos al usuario
        nombre = datos_basicos.pedir_nombre()
        edad = datos_basicos.pedir_edad()

        # Validar edad
        if validaciones.validar_edad(edad):
            # Guardar datos si son válidos
            gestion_datos.guardar_datos(nombre, edad)
        else:
            print("❌ Edad inválida, intente nuevamente.")

    elif opcion == "2":
        # Mostrar lista de datos guardados
        gestion_datos.listar_datos()

    else:
        print("Saliendo del sistema...")

if __name__ == "__main__":
    main()
