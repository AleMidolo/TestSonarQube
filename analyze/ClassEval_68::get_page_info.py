class PageUtil: 
    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.
        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
        """
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

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
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]
    
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
        results = [item for item in self.data if keyword in str(item)]
        num_results = len(results)
        num_pages = (num_results + self.page_size - 1) // self.page_size
    
        search_info = {
            "keyword": keyword,
            "total_results": num_results,
            "total_pages": num_pages,
            "results": results
        }
        return search_info
    
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
        
        current_page_data = self.get_page(page_number)
        
        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": page_number > 1,
            "has_next": page_number < self.total_pages,
            "data": current_page_data
        }