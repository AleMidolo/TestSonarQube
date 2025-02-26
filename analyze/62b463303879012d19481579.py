def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    import re

    # Regular expression to find number and supplement
    match = re.search(r'(\d+)([a-zA-Z]*)', issue)
    
    if match:
        number = match.group(1)
        supplement = match.group(2) if match.group(2) else None
        return number, supplement
    return None, None