def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    number = None
    suppl = None
    
    # Assuming 'issue' is a string or a dictionary-like object
    if isinstance(issue, str):
        # Extract number and suppl from the string
        # Example logic (customize based on actual format)
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                number = int(part)
            elif part.lower().startswith('suppl'):
                suppl = part
    
    elif isinstance(issue, dict):
        # Extract number and suppl from the dictionary
        number = issue.get('number')
        suppl = issue.get('suppl')
    
    return number, suppl