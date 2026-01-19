def search(self, keyword):
    """
    Busca elementos en los datos que contengan la palabra clave dada.
    :param keyword: str, la palabra clave a buscar
    :return: dict, que contiene información de búsqueda como el total de resultados y los elementos coincidentes
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
    
    # Search for elements that contain the keyword
    results = [item for item in self.data if keyword_str in str(item)]
    
    # Calculate total results
    total_results = len(results)
    
    # Calculate total pages based on page size
    total_pages = (total_results + self.page_size - 1) // self.page_size if total_results > 0 else 0
    
    # Create and return search info dictionary
    search_info = {
        "keyword": keyword_str,
        "total_results": total_results,
        "total_pages": total_pages,
        "results": results
    }
    
    return search_info