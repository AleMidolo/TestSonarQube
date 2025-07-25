import re

def make_find_paths(find_paths):
    """
    Dati una sequenza di percorsi frammentati o pattern passati tramite `--find`, trasforma tutti i percorsi frammentati in pattern glob. Lascia invariati i pattern già esistenti.

    Ad esempio, dato `find_paths` come:
      ['foo.txt', 'pp:root/somedir']

    ... trasforma in:
      ['sh:**/*foo.txt*/**', 'pp:root/somedir']
    """
    transformed_paths = []
    for path in find_paths:
        if re.match(r'^[a-zA-Z]+:', path):
            # Se il percorso inizia con un prefisso (es. 'pp:'), lo lascia invariato
            transformed_paths.append(path)
        else:
            # Altrimenti, trasforma il percorso in un pattern glob
            transformed_paths.append(f'sh:**/*{path}*/**')
    return transformed_paths