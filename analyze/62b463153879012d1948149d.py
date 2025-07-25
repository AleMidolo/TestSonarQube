def _explore_folder(folder):  
    """
    Obtiene los datos de los paquetes desde la carpeta.  

    Agrupa los archivos por el nombre base de su archivo XML y devuelve los datos en formato de diccionario.  

    Parámetros  
    ----------  
    folder : str  
        Carpeta del paquete  

    Retorna  
    -------  
    dict  
    """
    import os
    import xml.etree.ElementTree as ET

    data = {}
    
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            base_name = os.path.splitext(filename)[0]
            file_path = os.path.join(folder, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()
            data[base_name] = {child.tag: child.text for child in root}
    
    return data