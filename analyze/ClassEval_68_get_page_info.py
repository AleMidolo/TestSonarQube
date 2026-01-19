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
    import math
    
    # Calculate total items and total pages
    total_items = len(self.data)
    total_pages = math.ceil(total_items / self.per_page) if self.per_page > 0 else 0
    
    # Calculate start and end indices for the current page
    start_index = (page_number - 1) * self.per_page
    end_index = start_index + self.per_page
    
    # Get data for the current page
    page_data = self.data[start_index:end_index]
    
    # Determine if there are previous and next pages
    has_previous = page_number > 1
    has_next = page_number < total_pages
    
    return {
        "current_page": page_number,
        "per_page": self.per_page,
        "total_pages": total_pages,
        "total_items": total_items,
        "has_previous": has_previous,
        "has_next": has_next,
        "data": page_data
    }