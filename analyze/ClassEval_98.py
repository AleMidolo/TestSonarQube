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

    def process_xml_data(self, file_name):
        self.uppercase_item_texts()
        return self.write_xml(file_name)

    def uppercase_item_texts(self):
        for element in self.root.iter('item'):
            element.text = self.uppercase_text(element.text)

    @staticmethod
    def uppercase_text(text):
        return text.upper() if text else text

    def find_element(self, element_name):
        return self.root.findall(element_name)