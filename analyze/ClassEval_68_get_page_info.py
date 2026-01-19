def get_page_info(self, page_number):
    """
        Recupera informazioni su una pagina specifica.
        :param page_number: int, il numero della pagina per cui recuperare informazioni
        :return: dict, contenente informazioni sulla pagina come numero della pagina corrente, pagine totali, ecc.
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page_info(1)
        >>> {
        >>>     "current_page": 1,
        >>>     "per_page": 1,
        >>>     "total_pages": 4,
        >>>     "total_items": 4,
        >>>     "has_previous": False,
        >>>     "has_next": True,
        >>>     "data": [1]
        >>> }
        """
    if page_number < 1 or page_number > self.total_pages:
        return {}
    data = self.get_page(page_number)
    return {'current_page': page_number, 'per_page': self.page_size, 'total_pages': self.total_pages, 'total_items': self.total_items, 'has_previous': page_number > 1, 'has_next': page_number < self.total_pages, 'data': data}