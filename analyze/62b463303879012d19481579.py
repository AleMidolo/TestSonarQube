def _extract_number_and_supplment_from_issue_element(issue):
    """
    Estrai i possibili valori di numero e supplemento dai issue.

    Args:
        issue (str): La stringa contenente il numero e il supplemento.

    Returns:
        tuple: Una tupla contenente il numero (int) e il supplemento (str).
               Se il supplemento non è presente, il secondo elemento sarà None.
    """
    # Split the issue into parts based on spaces
    parts = issue.split()
    
    # Initialize number and supplement
    number = None
    supplement = None
    
    # Iterate through the parts to find the number and supplement
    for part in parts:
        if part.isdigit():
            number = int(part)
        else:
            supplement = part
    
    return number, supplement