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
    
    processed_list = []
    for item in input_list:
        if not isinstance(item, str):
            raise TypeError("All elements in the list must be strings.")
        
        if len(item) > 1 and item[-1] == os.sep:
            processed_list.append(item[:-1])
        else:
            processed_list.append(item)
    
    return processed_list