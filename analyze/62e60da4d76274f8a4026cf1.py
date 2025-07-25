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
        return list(self.record.values())
    
    return [self.record[key] for key in keys if key in self.record]