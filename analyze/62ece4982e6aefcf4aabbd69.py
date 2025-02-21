def _replace_register(flow_params, register_number, register_value):
    """
    Sostituisci il valore dai flussi con il numero di registro specificato.

    La chiave `register_value` nel dizionario verrà sostituita dal numero di registro specificato da `register_number`.

    :param flow_params: Dizionario contenente i flussi definiti  
    :param register_number: Il numero del registro in cui il valore verrà memorizzato  
    :param register_value: Chiave da sostituire con il numero di registro  
    """
    if register_value in flow_params:
        flow_params[register_value] = register_number
    return flow_params