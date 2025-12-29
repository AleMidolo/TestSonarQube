def get_page_info(self, page_number):
    """
        एक विशेष पृष्ठ के बारे में जानकारी प्राप्त करें।
        :param page_number: int, उस पृष्ठ का नंबर जिसके बारे में जानकारी प्राप्त करनी है
        :return: dict, जिसमें पृष्ठ की जानकारी जैसे वर्तमान पृष्ठ संख्या, कुल पृष्ठ, आदि शामिल हैं।
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