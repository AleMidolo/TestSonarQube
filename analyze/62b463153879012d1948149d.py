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
    
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            base_name = os.path.splitext(filename)[0]
            file_groups[base_name].append(os.path.join(folder, filename))
    
    return dict(file_groups)