def _replace_register(flow_params, register_number, register_value):
    """
    Sostituisci il valore dai flussi con il numero di registro specificato.

    La chiave `register_value` nel dizionario verrà sostituita dal numero di registro specificato da `register_number`.

    :param flow_params: Dizionario contenente i flussi definiti  
    :param register_number: Il numero del registro in cui il valore verrà memorizzato  
    :param register_value: Chiave da sostituire con il numero di registro  
    """
    # Itera su tutti i flussi nel dizionario
    for flow in flow_params.values():
        # Se il flusso è un dizionario e contiene il valore da sostituire
        if isinstance(flow, dict) and register_value in flow:
            # Sostituisci il valore con il numero di registro
            flow[register_value] = register_number
            
    return flow_params