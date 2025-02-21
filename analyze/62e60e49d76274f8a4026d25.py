def unit_of_work(metadata=None, timeout=None):
    from neo4j import GraphDatabase

    def decorator(func):
        def wrapper(*args, **kwargs):
            driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
            with driver.session() as session:
                with session.begin_transaction() as tx:
                    if metadata is not None:
                        tx.metadata = metadata
                    if timeout is not None:
                        tx.timeout = timeout
                    return func(tx, *args, **kwargs)
        return wrapper
    return decorator