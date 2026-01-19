def search(self, keyword):
    """
    डेटा में उन आइटमों की खोज करें जो दिए गए कीवर्ड को शामिल करते हैं।
    :param keyword: str, खोजने के लिए कीवर्ड
    :return: dict, खोज की जानकारी जैसे कुल परिणाम और मिलते-जुलते आइटम
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
    results = []
    for item in self.data:
        if keyword_str in str(item):
            results.append(item)
    
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