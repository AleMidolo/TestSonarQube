def search(self, keyword):
    """
    Cerca gli elementi nei dati che contengono la parola chiave fornita.
    :param keyword: str, la parola chiave da cercare
    :return: dict, contenente informazioni sulla ricerca come risultati totali e elementi corrispondenti
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
    
    # Search for items that contain the keyword
    results = [item for item in self.data if keyword_str in str(item)]
    
    # Calculate total results and total pages
    total_results = len(results)
    total_pages = (total_results + self.page_size - 1) // self.page_size if self.page_size > 0 else 0
    
    # Create and return the search info dictionary
    search_info = {
        "keyword": keyword,
        "total_results": total_results,
        "total_pages": total_pages,
        "results": results
    }
    
    return search_info