def write_xml(self, file_name):
        """
        निर्दिष्ट फ़ाइल में XML डेटा लिखता है।
        :param file_name: स्ट्रिंग, XML डेटा लिखने के लिए फ़ाइल का नाम।
        :return: बूल, यदि लिखने का कार्य सफल होता है तो True, अन्यथा False.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.write_xml('output.xml')
        >>> print(success)
        True
        """
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            return False