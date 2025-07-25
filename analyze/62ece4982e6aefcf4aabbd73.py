def split(s, platform='this'):
    import re
    import sys
    
    # Determine platform
    if platform == 'this':
        platform = 0 if sys.platform.startswith('win') else 1
    
    if platform == 1: # POSIX style
        # Handle escaped quotes and spaces
        s = s.replace('\\"','\x00').replace("\\'",'\x01')
        
        # Split on spaces while preserving quoted strings
        pattern = r'''(?:[^\s"'\\]|\\.|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')+'''
        parts = re.findall(pattern, s)
        
        # Restore escaped characters and remove surrounding quotes
        result = []
        for part in parts:
            if (part.startswith('"') and part.endswith('"')) or \
               (part.startswith("'") and part.endswith("'")):
                part = part[1:-1]
            part = part.replace('\x00','"').replace('\x01',"'")
            result.append(part)
            
    else: # Windows/CMD style
        # Split on spaces while preserving quoted strings
        pattern = r'''(?:[^\s"]|"(?:\\.|[^"\\])*")+'''
        parts = re.findall(pattern, s)
        
        # Remove surrounding quotes
        result = []
        for part in parts:
            if part.startswith('"') and part.endswith('"'):
                part = part[1:-1]
            result.append(part)
    
    return result