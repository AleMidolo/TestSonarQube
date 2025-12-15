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
        legge un file JSON e elabora i dati rimuovendo una chiave specificata e riscrivendo i dati modificati nel file.

        :param file_path: str, il percorso del file JSON.
        :param remove_key: str, la chiave da rimuovere.
        :return: 1, se la chiave specificata è stata rimossa con successo e i dati sono stati riscritti.
                    0, se il file non esiste o la chiave specificata non esiste nei dati.
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
        
        del data[remove_key]
        self.write_json(data, file_path)
        return 1