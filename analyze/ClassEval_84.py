import json


class TextFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_as_json(self):
        return self._read_file_with_json()

    def read_file(self):
        return self._read_file()

    def write_file(self, content):
        self._write_file(content)

    def process_file(self):
        content = self.read_file()
        processed_content = self._remove_non_alpha(content)
        self.write_file(processed_content)
        return processed_content

    def _read_file_with_json(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def _write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    def _remove_non_alpha(self, content):
        return ''.join(char for char in content if char.isalpha())