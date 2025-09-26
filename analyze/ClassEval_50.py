import json
import os


class JSONProcessor:
    SUCCESS = 1
    FILE_NOT_FOUND = 0
    ERROR = -1

    def read_json(self, file_path):
        if not os.path.exists(file_path):
            return self.FILE_NOT_FOUND
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return self.ERROR

    def write_json(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            return self.SUCCESS
        except Exception:
            return self.ERROR

    def process_json(self, file_path, remove_key):
        data = self.read_json(file_path)
        if self.is_error(data):
            return self.FILE_NOT_FOUND
        if self.remove_key_from_data(data, remove_key):
            return self.write_json(data, file_path)
        return self.FILE_NOT_FOUND

    def is_error(self, data):
        return data == self.FILE_NOT_FOUND or data == self.ERROR

    def remove_key_from_data(self, data, remove_key):
        if remove_key in data:
            del data[remove_key]
            return True
        return False