# Módulo para validar datos ingresados.

def validar_edad(edad):
    # Verifica que la edad sea un número entero positivo
    try:
        edad_int = int(edad)
        return edad_int > 0
    except ValueError:
        return False
