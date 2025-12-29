def search(self, keyword):
    """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.search("1")
        >>> search_info = {
        >>>     "keyword": "1",
        >>>     "total_results": 1,
        >>>     "total_pages": 1,
        >>>     "results": [1]
        >>> }
        """
    keyword_str = str(keyword)
    matching_items = []
    for item in self.data:
        if keyword_str in str(item):
            matching_items.append(item)
    total_results = len(matching_items)
    total_pages = (total_results + self.page_size - 1) // self.page_size if total_results > 0 else 0
    search_info = {'keyword': keyword_str, 'total_results': total_results, 'total_pages': total_pages, 'results': matching_items}
    return search_info