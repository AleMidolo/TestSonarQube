def get_page_info(self, page_number):
    """
        获取特定页面的信息。
        :param page_number: int, 要获取信息的页面编号
        :return: dict, 包含页面信息，如当前页面编号、总页面数等。
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
    page_data = self.get_page(page_number)
    page_info = {'current_page': page_number, 'per_page': self.page_size, 'total_pages': self.total_pages, 'total_items': self.total_items, 'has_previous': page_number > 1, 'has_next': page_number < self.total_pages, 'data': page_data}
    return page_info