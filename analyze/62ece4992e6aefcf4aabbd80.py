import os

def remove_ending_os_sep(input_list):
    """
    Iterate over a string list and remove trailing os seperator characters.

    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator. If so, the pathname seperator character
    is removed.

    Args:
        input_list: list of strings

    Returns:
        Processed list of strings

    Raises:
        TypeError
    """
    if input_list is None:
        return []
    
    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list")
    
    return [s.rstrip(os.sep) for s in input_list if len(s) > 1]