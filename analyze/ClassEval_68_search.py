def search(self, keyword):
    """
    在数据中搜索包含给定关键字的项目。
    :param keyword: str, 要搜索的关键字
    :return: dict, 包含搜索信息，如总结果和匹配的项目
    >>> page_util = PageUtil([1, 2, 3, 4], 1)
    >>> page_util.search("1")
    >>> search_info = {
    >>>     "keyword": "1",
    >>>     "total_results": 1,
    >>>     "total_pages": 1,
    >>>     "results": [1]
    >>> }
    """
    # 将关键字转换为字符串以便搜索
    keyword_str = str(keyword)
    
    # 搜索匹配的项目
    results = []
    for item in self.data:
        # 将每个项目转换为字符串并检查是否包含关键字
        if keyword_str in str(item):
            results.append(item)
    
    # 计算总结果数
    total_results = len(results)
    
    # 计算总页数
    if total_results == 0:
        total_pages = 0
    else:
        total_pages = (total_results + self.page_size - 1) // self.page_size
    
    # 返回搜索信息
    search_info = {
        "keyword": keyword,
        "total_results": total_results,
        "total_pages": total_pages,
        "results": results
    }
    
    return search_info