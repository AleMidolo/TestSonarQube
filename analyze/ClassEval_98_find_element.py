def find_element(self, element_name):
    """
    查找具有指定名称的 XML 元素。
    :param element_name: 字符串，要查找的元素名称。
    :return: 列表，具有指定名称的找到的元素列表。
    >>> xml_processor = XMLProcessor('test.xml')
    >>> root = xml_processor.read_xml()
    >>> items = xml_processor.find_element('item')
    >>> for item in items:
    >>>     print(item.text)
    apple
    banana
    orange
    """
    if hasattr(self, 'root') and self.root is not None:
        return self.root.findall('.//' + element_name)
    return []