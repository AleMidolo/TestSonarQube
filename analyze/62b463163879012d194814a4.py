import zipfile
import os
from collections import defaultdict

def _explore_zipfile(zip_path):
    """
    Ottiene i dati dei pacchetti dal percorso zip fornito.

    Raggruppa i file in base al nome base dei loro file XML e restituisce i dati in formato dizionario.

    Parametri
    ----------
    zip_path : str  
        Percorso del file zip.

    Restituisce
    -------
    dict
        Un dizionario che raggruppa i file in base al nome base dei loro file XML.
    """
    data = defaultdict(list)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.xml'):
                base_name = os.path.basename(file_name)
                data[base_name].append(file_name)
    
    return dict(data)