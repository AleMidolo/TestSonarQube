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
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list of strings.")
    
    os_sep = os.path.sep
    return [s[:-1] if len(s) > 1 and s.endswith(os_sep) else s for s in input_list]