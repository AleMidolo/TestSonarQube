def _extract_number_and_supplment_from_issue_element(issue):
    number = None
    suppl = None
    
    if 'number' in issue:
        number = issue['number']
    
    if 'suppl' in issue:
        suppl = issue['suppl']
    
    return number, suppl