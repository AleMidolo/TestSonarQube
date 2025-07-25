import re

def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    # Regular expression to extract number and suppl from the issue content
    pattern = r'(?P<number>\d+)(?:\s*\((?P<suppl>[^)]+)\))?'
    match = re.search(pattern, issue)
    
    if match:
        number = match.group('number')
        suppl = match.group('suppl') if match.group('suppl') else None
        return number, suppl
    else:
        return None, None