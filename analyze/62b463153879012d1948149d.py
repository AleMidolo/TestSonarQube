def _explore_folder(folder):  
    """
    Ottiene i dati dei pacchetti dalla cartella  

    Raggruppa i file in base al loro nome base XML e restituisce i dati in formato dizionario.  

    Parametri  
    ----------  
    folder : str  
        Cartella del pacchetto  

    Restituisce  
    -------  
    dict  
    """
    import os
    import xml.etree.ElementTree as ET
    from collections import defaultdict

    package_data = defaultdict(list)

    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            base_name = os.path.splitext(filename)[0]
            file_path = os.path.join(folder, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                package_data[base_name].append(root)
            except ET.ParseError as e:
                print(f"Error parsing {file_path}: {e}")

    return dict(package_data)