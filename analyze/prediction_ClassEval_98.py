import xml.etree.ElementTree as ET


class XMLProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except ET.ParseError:
            return None

    def write_xml(self, file_name):
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception:
            return False

    def process_xml_data(self, output_file_name):
        self._convert_items_to_uppercase()
        return self.write_xml(output_file_name)

    def _convert_items_to_uppercase(self):
        for element in self.root.iter('item'):
            element.text = self._to_uppercase(element.text)

    def _to_uppercase(self, text):
        return text.upper() if text else text

    def find_element(self, element_name):
        return self.root.findall(element_name)