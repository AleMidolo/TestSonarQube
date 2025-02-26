def unit_of_work(metadata=None, timeout=None):
    """
    Esta función es un decorador para funciones de transacción que permite un control adicional sobre cómo se lleva a cabo la transacción.

    Por ejemplo, se puede aplicar un tiempo de espera (timeout)::

    from neo4j import unit_of_work

    @unit_of_work(timeout=100)
    def count_people_tx(tx):
        result = tx.run("MATCH (a:Person) RETURN count(a) AS persons")
        record = result.single()
        return record["persons"]

    :param metadata:
    Un diccionario con metadatos.  
    Los metadatos especificados se adjuntarán a la transacción en ejecución y serán visibles en la salida de los procedimientos ``dbms.listQueries`` y ``dbms.listTransactions``.  
    También se registrarán en el archivo ``query.log``.  
    Esta funcionalidad facilita etiquetar transacciones y es equivalente al procedimiento ``dbms.setTXMetaData``. Consulte la referencia del procedimiento en: https://neo4j.com/docs/operations-manual/current/reference/procedures/.  
    :type metadata: dict  

    :param timeout:  
    El tiempo de espera de la transacción en segundos.  
    Las transacciones que se ejecuten durante más tiempo que el tiempo de espera configurado serán terminadas por la base de datos.  
    Esta funcionalidad permite limitar el tiempo de ejecución de consultas/transacciones.  
    El tiempo de espera especificado sobrescribe el tiempo de espera predeterminado configurado en la base de datos mediante la configuración ``dbms.transaction.timeout``.  
    El valor no debe representar una duración negativa.  
    Una duración de cero hará que la transacción se ejecute indefinidamente.  
    Un valor de `None` utilizará el tiempo de espera predeterminado configurado en la base de datos.  
    :type timeout: float o :const:`None`
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Aquí se implementaría la lógica para manejar la transacción
            # y aplicar los metadatos y el tiempo de espera.
            pass  # Lógica de la transacción aquí
        return wrapper
    return decorator