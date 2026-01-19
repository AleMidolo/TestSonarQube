import json

def write_json(self, data, file_path):
    """
    Scrive i dati in un file JSON e lo salva nel percorso fornito.

    :param data: dict, i dati da scrivere nel file JSON.
    :param file_path: str, il percorso del file JSON.
    :return: 1 se il processo di scrittura ha successo, o -1 se si verifica un errore durante il processo di scrittura.
    >>> json.write_json({'key1': 'value1', 'key2': 'value2'}, 'test.json')
    1
    >>> json.read_json('test.json')
    {'key1': 'value1', 'key2': 'value2'}
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return 1
    except Exception:
        return -1