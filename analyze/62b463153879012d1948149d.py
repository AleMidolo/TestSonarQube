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
    from collections import defaultdict
    
    # Dizionario per raggruppare i file per nome base
    files_by_base = defaultdict(list)
    
    # Esplora tutti i file nella cartella
    for file in os.listdir(folder):
        if file.endswith('.xml'):
            # Ottieni il nome base rimuovendo l'estensione
            base_name = os.path.splitext(file)[0]
            # Aggiungi il percorso completo del file alla lista del nome base
            files_by_base[base_name].append(os.path.join(folder, file))
            
    # Converti defaultdict in dict normale
    return dict(files_by_base)