def was_processed(processed, path_name, verbose):
    """
    यहाँ फ़ंक्शन का कार्यान्वयन होगा
    """
    if verbose:
        print(f"Checking if '{path_name}' was processed...")
    
    if path_name in processed:
        if verbose:
            print(f"'{path_name}' was already processed.")
        return True
    else:
        if verbose:
            print(f"'{path_name}' was not processed.")
        return False