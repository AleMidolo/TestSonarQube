def get_page(self, page_number):
    """
    Recupera una pagina specifica di dati.
    :param page_number: int, il numero della pagina da recuperare
    :return: list, i dati sulla pagina specificata
    >>> page_util = PageUtil([1, 2, 3, 4], 1)
    >>> page_util.get_page(1)
    [1]

    """
    if page_number < 1:
        return []
    
    start_index = (page_number - 1) * self.page_size
    end_index = start_index + self.page_size
    
    if start_index >= len(self.data):
        return []
    
    return self.data[start_index:end_index]