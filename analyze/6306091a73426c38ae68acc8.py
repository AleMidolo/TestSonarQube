from typing import List, Dict, Any

def list_of_file_names(settings_dirs: List[str], spec_option: str) -> List[str]:
    """
    Crea un nuevo tipo complejo "IniType".

    Args:
        settings_dirs (List[str]): Lista de directorios donde buscar archivos de configuración.
        spec_option (str): Opción específica para filtrar los archivos.

    Returns:
        List[str]: Lista de nombres de archivos que cumplen con la opción específica.
    """
    import os
    file_names = []
    
    for directory in settings_dirs:
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                if spec_option in file:
                    file_names.append(file)
    
    return file_names