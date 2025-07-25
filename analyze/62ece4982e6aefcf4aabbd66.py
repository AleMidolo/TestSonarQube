def was_processed(processed, path_name, verbose):
    """
    यहाँ फ़ंक्शन का कार्यान्वयन होगा
    """
    if path_name in processed:
        if verbose:
            print(f"'{path_name}' has already been processed.")
        return True
    else:
        processed.add(path_name)
        if verbose:
            print(f"'{path_name}' is being processed for the first time.")
        return False