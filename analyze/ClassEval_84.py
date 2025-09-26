import json


class TextFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_as_json(self):
        return self._load_json(self.file_path)

    def read_file(self):
        return self._read_file_content(self.file_path)

    def write_file(self, content):
        self._write_file_content(self.file_path, content)

    def process_file(self):
        content = self.read_file()
        processed_content = self._remove_non_alpha(content)
        self.write_file(processed_content)
        return processed_content

    def _load_json(self, path):
        with open(path, 'r') as file:
            return json.load(file)

    def _read_file_content(self, path):
        with open(path, 'r') as file:
            return file.read()

    def _write_file_content(self, path, content):
        with open(path, 'w') as file:
            file.write(content)

    def _remove_non_alpha(self, content):
        return ''.join(char for char in content if char.isalpha())