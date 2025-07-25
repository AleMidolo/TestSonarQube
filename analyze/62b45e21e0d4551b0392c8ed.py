import os

def find_path_type(path):
    """
    Devuelve una cadena que indica el tipo de elemento en la ruta proporcionada.

    Valores de retorno:
        'root' - parece ser una Raíz de Almacenamiento OCFL
        'object' - parece ser un Objeto OCFL
        'file' - un archivo, podría ser un inventario
        otra cadena explica la descripción del error

    Solo examina los archivos "0=*" Namaste para determinar el tipo de directorio.
    """
    if not os.path.exists(path):
        return "La ruta no existe."
    
    if os.path.isfile(path):
        return "file"
    
    namaste_files = [f for f in os.listdir(path) if f.startswith("0=")]
    
    if not namaste_files:
        return "No se encontraron archivos Namaste en la ruta."
    
    for namaste_file in namaste_files:
        with open(os.path.join(path, namaste_file), 'r') as f:
            content = f.read().strip()
            if content == "ocfl_object_1.0":
                return "object"
            elif content == "ocfl_1.0":
                return "root"
    
    return "No se pudo determinar el tipo de la ruta basado en los archivos Namaste."