def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    # Initialize empty values
    number = None
    suppl = None
    
    # If issue is None or empty, return default values
    if not issue:
        return number, suppl
        
    # Convert issue to string and remove whitespace
    issue_text = str(issue).strip()
    
    # Check if issue contains supplement indicator
    if 'suppl' in issue_text.lower():
        # Extract supplement value
        suppl_parts = issue_text.lower().split('suppl')
        if len(suppl_parts) > 1:
            suppl = suppl_parts[1].strip()
            # Extract number from first part if exists
            if suppl_parts[0].strip():
                number = suppl_parts[0].strip()
    else:
        # If no supplement, treat entire text as number
        number = issue_text
        
    # Clean up number and supplement values
    if number:
        number = number.strip(' .,;')
    if suppl:
        suppl = suppl.strip(' .,;')
        
    return number, suppl