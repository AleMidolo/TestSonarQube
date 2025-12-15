import json
import os

class JSONProcessor: 

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :param file_path: str, the path of the JSON file.
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
    
        if not os.path.exists(file_path):
            return 0
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except:
            return -1
    
    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.
    
        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: 1 if the writing process is successful, or -1, if an error occurs during the writing process.
        >>> json.write_json({'key1': 'value1', 'key2': 'value2'}, 'test.json')
        1
        >>> json.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        """
    
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            return 1
        except:
            return -1
    
    def process_json(self, file_path, remove_key):
        """
        读取一个 JSON 文件，并通过移除指定的键来处理数据，并将修改后的数据重新写回文件。

        :param file_path: str，JSON 文件的路径。
        :param remove_key: str，要移除的键。
        :return: 1，如果成功移除指定的键并将数据写回。
                    0，如果文件不存在或指定的键在数据中不存在。
        >>> json.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        >>> json.process_json('test.json', 'key1')
        1
        >>> json.read_json('test.json')
        {'key2': 'value2'}
        """
        data = self.read_json(file_path)
        if data == 0 or remove_key not in data:
            return 0
        data.pop(remove_key)
        self.write_json(data, file_path)
        return 1