def find_element(self, element_name):
    """
        निर्दिष्ट नाम के साथ XML तत्वों को खोजता है।
        :param element_name: स्ट्रिंग, खोजने के लिए तत्वों का नाम।
        :return: सूची, निर्दिष्ट नाम के साथ पाए गए तत्वों की सूची।
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_element('item')
        >>> for item in items:
        >>>     print(item.text)
        apple
        banana
        orange
        """
    if self.root is None:
        return []
    found_elements = []
    for element in self.root.iter(element_name):
        found_elements.append(element)
    return found_elements