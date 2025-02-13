def paging(response, max_results):
    """
    Restituisce la risposta WAPI pagina per pagina
        Argomenti: 
        response (list): Risposta WAPI.  
        max_results (int): Numero massimo di oggetti da restituire in una singola pagina.  

        Restituisce: 
        Oggetto generatore con la risposta WAPI suddivisa pagina per pagina.  
    """
    for i in range(0, len(response), max_results):
        yield response[i:i + max_results]