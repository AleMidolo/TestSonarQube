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
            # Get supplement number after 'suppl'
            suppl = suppl_parts[1].strip()
            # Remove any non-numeric characters
            suppl = ''.join(c for c in suppl if c.isdigit())
            if suppl:
                suppl = int(suppl)
            
        # Get number before 'suppl' if it exists
        number_part = suppl_parts[0].strip()
        if number_part:
            # Remove any non-numeric characters
            number = ''.join(c for c in number_part if c.isdigit())
            if number:
                number = int(number)
                
    else:
        # If no supplement, extract just the number
        number = ''.join(c for c in issue_text if c.isdigit())
        if number:
            number = int(number)
            
    return number, suppl