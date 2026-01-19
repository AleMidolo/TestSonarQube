def get_page(self, page_number):
    """
    Recupera una página específica de datos.
    :param page_number: int, el número de página a obtener
    :return: list, los datos en la página especificada
    >>> page_util = PageUtil([1, 2, 3, 4], 1)
    >>> page_util.get_page(1)
    [1]

    """
    if page_number < 1 or page_number > self.total_pages:
        return []
    
    start_index = (page_number - 1) * self.page_size
    end_index = start_index + self.page_size
    
    return self.data[start_index:end_index]