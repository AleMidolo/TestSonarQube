def was_processed(processed, path_name, verbose):
    """
    यहाँ फ़ंक्शन का कार्यान्वयन होगा
    """
    try:
        # Check if path_name exists in processed dictionary
        if path_name in processed:
            if verbose:
                print(f"File {path_name} was already processed")
            return True
        return False
    except Exception as e:
        if verbose:
            print(f"Error checking if {path_name} was processed: {str(e)}")
        return False