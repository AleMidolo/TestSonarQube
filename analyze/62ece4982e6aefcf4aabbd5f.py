def paging(response, max_results):
    """
    Devuelve la respuesta de WAPI página por página.

    Argumentos:
        response (list): Respuesta de WAPI.
        max_results (int): Número máximo de objetos que se devolverán en una página.

    Retorna:
        Objeto generador con la respuesta de WAPI dividida página por página.
    """
    for i in range(0, len(response), max_results):
        yield response[i:i + max_results]