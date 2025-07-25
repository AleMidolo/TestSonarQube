def values(self, *keys):
    """
    Return the values of the record, optionally filtering to
    include only certain values by index or key.

    :param keys: indexes or keys of the items to include; if none
                 are provided, all values will be included
    :return: list of values
    :rtype: list
    """
    if not keys:
        return list(self.__dict__.values())
    else:
        return [self.__dict__[key] if isinstance(key, str) else list(self.__dict__.values())[key] for key in keys]