import re

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
        if re.match(r'^[a-zA-Z]+:', path):
            # Si el path ya tiene un prefijo (como 'pp:'), lo dejamos sin modificar
            transformed_paths.append(path)
        else:
            # Si no tiene prefijo, lo transformamos en un patrón glob
            transformed_paths.append(f'sh:**/*{path}*/**')
    return transformed_paths