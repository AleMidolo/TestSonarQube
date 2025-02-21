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
        if ':' in path:  # Check if it's a pattern
            transformed_paths.append(path)
        else:  # Transform fragmented path to glob pattern
            transformed_paths.append(f'sh:**/*{path}*/**')
    return transformed_paths