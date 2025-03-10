def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    Insieme alla funzione :func:`generate_default_observer_schema_list`, questa funzione viene chiamata ricorsivamente per generare una parte dello schema predefinito `observer_schema` a partire da una risorsa Kubernetes, definita rispettivamente da `manifest_dict` o `manifest_list`.

    ### Argomenti:
    - **manifest_dict (dict)**: Risorse Kubernetes parziali.
    - **first_level (bool, opzionale)**: Se impostato su True, indica che il dizionario rappresenta l'intero schema `observer_schema` di una risorsa Kubernetes.

    ### Ritorna:
    - **dict**: Lo schema parziale `observer_schema` generato.

    Questa funzione crea un nuovo dizionario a partire da `manifest_dict` e sostituisce tutti i valori che non sono liste o dizionari con `None`.

    Nel caso di un dizionario `first_level` (ovvero lo schema completo `observer_schema` per una risorsa), i valori dei campi identificativi vengono copiati dal file manifest.
    """
    observer_schema = {}
    
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value)
        elif isinstance(value, list):
            observer_schema[key] = generate_default_observer_schema_list(value)
        else:
            if first_level and key in ['apiVersion', 'kind', 'metadata']:
                observer_schema[key] = value
            else:
                observer_schema[key] = None
    
    return observer_schema

def generate_default_observer_schema_list(manifest_list):
    """
    Funzione ausiliaria per gestire le liste all'interno del dizionario.
    """
    observer_schema = []
    
    for item in manifest_list:
        if isinstance(item, dict):
            observer_schema.append(generate_default_observer_schema_dict(item))
        elif isinstance(item, list):
            observer_schema.append(generate_default_observer_schema_list(item))
        else:
            observer_schema.append(None)
    
    return observer_schema