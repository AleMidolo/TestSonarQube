def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    number = None
    suppl = None
    
    if issue:
        # Remove any whitespace
        issue = issue.strip()
        
        # Check if issue contains supplement indicator
        if 'suppl' in issue.lower():
            parts = issue.lower().split('suppl')
            if parts[0]:
                number = parts[0].strip()
            if len(parts) > 1 and parts[1]:
                suppl = parts[1].strip()
        else:
            # If no supplement, treat entire string as number
            number = issue
            
        # Convert number to integer if possible
        try:
            number = int(number) if number else None
        except (ValueError, TypeError):
            number = number
            
        # Clean up supplement value
        if suppl:
            suppl = suppl.strip(' .')
            if suppl.startswith('.'):
                suppl = suppl[1:]
                
    return number, suppl