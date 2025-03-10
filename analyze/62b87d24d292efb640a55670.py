import sys

def get_versions():
    """
    Obtén la información de la versión o devuelve el valor predeterminado si no es posible obtenerla.
    """
    try:
        # Intentar obtener la versión de Python
        python_version = sys.version
        return {
            "python_version": python_version
        }
    except Exception as e:
        # Si ocurre un error, devolver un valor predeterminado
        return {
            "python_version": "Unknown"
        }