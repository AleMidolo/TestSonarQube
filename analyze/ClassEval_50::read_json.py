import json
import os

class JSONProcessor: 

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
        read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.
    
        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        >>> json.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        >>> json.process_json('test.json', 'key1')
        1
        >>> json.read_json('test.json')
        {'key2': 'value2'}
        """
    
        data = self.read_json(file_path)
        if data == 0 or data == -1:
            return 0
        if remove_key in data:
            del data[remove_key]
            self.write_json(data, file_path)
            return 1
        else:
            return 0
    
    def read_json(self, file_path):
        """
        Leggi un file JSON e restituisci i dati.
        :param file_path: str, il percorso del file JSON.
        :return: dict, i dati dal file JSON se letti con successo, oppure restituisce -1 se si verifica un errore durante il processo di lettura.
                    restituisce 0 se il file non esiste.
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
        if not os.path.exists(file_path):
            return 0
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except:
            return -1