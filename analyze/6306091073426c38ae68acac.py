def dict_insert(dic, val, key, *keys):
    """
    Inserta un valor en una llave anidada dentro de un diccionario.

    Para insertar un valor en una llave anidada, se deben proporcionar todas las llaves previas como argumentos del método.

    Ejemplo:
      dict_insert({}, 'val', 'key1.key2'.split('.'))

    :param dic: un objeto diccionario donde se insertará el valor de la llave anidada.
    :param val: un valor que se insertará en el diccionario dado.
    :param key: la primera llave en una cadena de llaves que almacenará el valor.
    :param keys: subllaves en la cadena de llaves.
    """
    for k in (key,) + keys:
        if k not in dic:
            dic[k] = {}
        dic = dic[k]
    dic[keys[-1]] = val