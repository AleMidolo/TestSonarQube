def make_find_paths(find_paths):
    """
    Dada una secuencia de fragmentos de rutas o patrones proporcionados a través de `--find`, transforma todos los fragmentos de rutas en patrones glob. Deja los patrones existentes sin modificar.

    Por ejemplo, dado un `find_paths` de:

      ['foo.txt', 'pp:root/somedir']

    ... se transforma en:

      ['sh:**/*foo.txt*/**', 'pp:root/somedir']
    """
    transformed_paths = []
    for path in find_paths:
        if not path.startswith('pp:'):
            transformed_path = f'sh:**/*{path}*/**'
            transformed_paths.append(transformed_path)
        else:
            transformed_paths.append(path)
    return transformed_paths