def unit_of_work(metadata=None, timeout=None):
    """
    Decorator for transaction functions that allows additional control over how the transaction is executed.

    For example, a timeout can be applied::

        from neo4j import unit_of_work

        @unit_of_work(timeout=100)
        def count_people_tx(tx):
            result = tx.run("MATCH (a:Person) RETURN count(a) AS persons")
            record = result.single()
            return record["persons"]

    :param metadata:  
        A dictionary with metadata.  
        The specified metadata will be associated with the executing transaction and visible in the output of the procedures ``dbms.listQueries`` and ``dbms.listTransactions``.  
        It will also be logged in the ``query.log`` file.  
        This feature simplifies labeling transactions and is equivalent to the procedure ``dbms.setTXMetaData``. For reference to the procedure, see https://neo4j.com/docs/operations-manual/current/reference/procedures/.  
    :type metadata: dict  

    :param timeout:  
        The transaction timeout in seconds.  
        Transactions that run longer than the configured timeout will be terminated by the database.  
        This feature allows limiting the execution time of queries/transactions.  
        The specified timeout overrides the default timeout configured in the database using the setting ``dbms.transaction.timeout``.  
        The value must not represent a negative duration.  
        A duration of zero will allow the transaction to run indefinitely.  
        A value of ``None`` will use the default timeout configured in the database.  
    :type timeout: float or :const:`None`  
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Here you would typically integrate with the Neo4j transaction management
            # For example, setting metadata and timeout on the transaction
            # This is a simplified example and may need to be adapted to your specific Neo4j setup
            tx = kwargs.get('tx', None)
            if tx:
                if metadata is not None:
                    tx.set_metadata(metadata)
                if timeout is not None:
                    tx.set_timeout(timeout)
            return func(*args, **kwargs)
        return wrapper
    return decorator