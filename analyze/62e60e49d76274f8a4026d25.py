def unit_of_work(metadata=None, timeout=None):
    """
    Questa funzione è un decorator per funzioni di transazione che consente un controllo aggiuntivo su come viene eseguita la transazione.

    Ad esempio, è possibile applicare un timeout::

        from neo4j import unit_of_work

        @unit_of_work(timeout=100)
        def count_people_tx(tx):
            result = tx.run("MATCH (a:Person) RETURN count(a) AS persons")
            record = result.single()
            return record["persons"]

    :param metadata:  
        un dizionario con metadati.  
        I metadati specificati saranno associati alla transazione in esecuzione e visibili nell'output delle procedure ``dbms.listQueries`` e ``dbms.listTransactions``.  
        Saranno inoltre registrati nel file ``query.log``.  
        Questa funzionalità semplifica l'etichettatura delle transazioni ed è equivalente alla procedura ``dbms.setTXMetaData``. Per riferimento alla procedura, consultare https://neo4j.com/docs/operations-manual/current/reference/procedures/.  
    :type metadata: dict  

    :param timeout:  
        il timeout della transazione in secondi.  
        Le transazioni che vengono eseguite per un tempo superiore al timeout configurato saranno terminate dal database.  
        Questa funzionalità consente di limitare il tempo di esecuzione delle query/transazioni.  
        Il timeout specificato sovrascrive il timeout predefinito configurato nel database utilizzando l'impostazione ``dbms.transaction.timeout``.  
        Il valore non deve rappresentare una durata negativa.  
        Una durata pari a zero consentirà alla transazione di essere eseguita indefinitamente.  
        Un valore ``None`` utilizzerà il timeout predefinito configurato nel database.  
    :type timeout: float o :const:`None`  
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Implementazione della logica per gestire la transazione
            # e applicare i metadati e il timeout
            pass  # Sostituire con la logica effettiva
        return wrapper
    return decorator