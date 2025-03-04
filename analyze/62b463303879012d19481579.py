def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    number = None
    suppl = None
    
    if issue:
        # Remove any whitespace
        issue = issue.strip()
        
        # Split on spaces to separate number and supplement
        parts = issue.split()
        
        if parts:
            # First part is the number
            number = parts[0]
            
            # Check for supplement in remaining parts
            if len(parts) > 1:
                suppl = ' '.join(parts[1:])
                
                # Remove parentheses if present
                suppl = suppl.strip('()')
    
    return number, suppl