import os

def was_processed(processed, path_name, verbose):
    """
    Verificar si un archivo o directorio ya ha sido procesado.

    Para evitar la recursión, expanda el nombre de la ruta a una ruta absoluta
    y llame a esta función con un conjunto que almacenará todas las entradas
    y la entrada a verificar. Si la entrada ya está en el conjunto, informe
    del problema y devuelva ``True``. De lo contrario, agregue la entrada al
    conjunto y devuelva ``False`` para permitir que la ruta sea procesada.

    Parámetros:
        processed: Conjunto para almacenar los nombres de ruta procesados.
        path_name: Ruta a un directorio o archivo.
        verbose: `True` si se solicita salida detallada.

    Devuelve:
        `True` si ya está en el conjunto.
        `False` si no lo está.
    """
    abs_path = os.path.abspath(path_name)
    if abs_path in processed:
        if verbose:
            print(f"La ruta '{abs_path}' ya ha sido procesada.")
        return True
    else:
        processed.add(abs_path)
        return False