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
        if ':' in path:  # Assuming patterns with ':' are already in the correct format
            transformed_paths.append(path)
        else:
            transformed_path = f'sh:**/*{path}*/**'
            transformed_paths.append(transformed_path)
    return transformed_paths