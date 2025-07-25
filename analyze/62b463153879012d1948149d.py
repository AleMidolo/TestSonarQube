import os
from collections import defaultdict

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
        Dizionario con i file raggruppati per nome base XML.
    """
    file_groups = defaultdict(list)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.xml'):
                base_name = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                file_groups[base_name].append(file_path)
    
    return dict(file_groups)