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
    results = [item for item in self.data if str(item) == keyword]
    total_results = len(results)
    total_pages = (total_results + self.page_size - 1) // self.page_size
    search_info = {'keyword': keyword, 'total_results': total_results, 'total_pages': total_pages, 'results': results}
    return search_info