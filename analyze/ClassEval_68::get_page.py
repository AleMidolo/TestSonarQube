def get_page(self, page_number):
    """
        Retrieve a specific page of data.
        :param page_number: int, the page number to fetch
        :return: list, the data on the specified page
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page(1)
        [1]

        """
    if page_number < 1 or page_number > self.total_pages:
        return []
    start_index = (page_number - 1) * self.page_size
    end_index = min(start_index + self.page_size, self.total_items)
    return self.data[start_index:end_index]