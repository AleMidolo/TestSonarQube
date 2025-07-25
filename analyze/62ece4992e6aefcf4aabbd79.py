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
            # If the path is already a pattern (e.g., 'pp:root/somedir'), leave it unchanged
            transformed_paths.append(path)
        else:
            # If the path is a fragment, transform it into a glob pattern
            transformed_paths.append(f'sh:**/*{path}*/**')
    return transformed_paths