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
    # Convert keyword to string for comparison
    keyword_str = str(keyword)
    
    # Filter items that contain the keyword
    results = [item for item in self.data if keyword_str in str(item)]
    
    # Calculate total results and pages
    total_results = len(results)
    total_pages = (total_results + self.page_size - 1) // self.page_size if total_results > 0 else 0
    
    # Return search information
    search_info = {
        "keyword": keyword,
        "total_results": total_results,
        "total_pages": total_pages,
        "results": results
    }
    
    return search_info