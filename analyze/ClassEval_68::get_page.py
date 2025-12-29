def get_page(self, page_number):
    """
        डेटा का एक विशिष्ट पृष्ठ प्राप्त करें।
        :param page_number: int, प्राप्त करने के लिए पृष्ठ संख्या
        :return: list, निर्दिष्ट पृष्ठ पर डेटा
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page(1)
        [1]

        """
    if page_number < 1 or page_number > self.total_pages:
        return []
    start_index = (page_number - 1) * self.page_size
    end_index = min(start_index + self.page_size, self.total_items)
    return self.data[start_index:end_index]