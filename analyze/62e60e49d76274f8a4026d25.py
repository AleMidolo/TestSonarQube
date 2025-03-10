def unit_of_work(metadata=None, timeout=None):
    """
    Decorator for transaction functions that allows additional control over how the transaction is executed.

    :param metadata: A dictionary with metadata. The specified metadata will be associated with the executing transaction and visible in the output of `dbms.listQueries` and `dbms.listTransactions`. It will also be logged in the `query.log` file.
    :type metadata: dict
    :param timeout: The transaction timeout in seconds. Transactions that run longer than the configured timeout will be terminated by the database. This feature allows limiting the execution time of queries/transactions. The specified timeout overrides the default timeout configured in the database using the `dbms.transaction.timeout` setting. The value must not be negative. A duration of zero will allow the transaction to run indefinitely. A value of `None` will use the default timeout configured in the database.
    :type timeout: float or None
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Here you would typically integrate with a transaction management system
            # For example, in Neo4j, you might use the session or transaction context
            # This is a simplified example
            if metadata is not None:
                kwargs['metadata'] = metadata
            if timeout is not None:
                kwargs['timeout'] = timeout
            return func(*args, **kwargs)
        return wrapper
    return decorator