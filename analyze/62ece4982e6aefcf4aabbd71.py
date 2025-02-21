import re

def regex_dict(item):
    """
    Converti le chiavi *.cpp in chiavi regex.

    Dato un dizionario in cui le chiavi sono tutti nomi di file con caratteri jolly, converti solo le chiavi in regex equivalenti e lascia intatti i valori.

    Esempio:

    rules = {
        '*.cpp':
            {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h':
            {'h': 'help'}
    }
    regex_keys = regex_dict(rules)

    Argomenti:
        item: dizionario da convertire
    Ritorna:
        dizionario con le chiavi convertite in regex.
    """
    regex_item = {}
    for key, value in item.items():
        regex_key = re.escape(key).replace(r'\*', '.*').replace(r'\?', '.')
        regex_item[regex_key] = value
    return regex_item