def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
    if not cmd:
        return cmd
        
    # Se il primo elemento è un file con shebang
    if cmd[0].endswith(('.py', '.sh')):
        # Su Windows aggiungiamo python/bash come interprete
        import sys
        import os
        
        if sys.platform == 'win32':
            ext = os.path.splitext(cmd[0])[1].lower()
            
            if ext == '.py':
                return ('python',) + cmd
            elif ext == '.sh':
                # Per script bash su Windows
                return ('bash',) + cmd
                
    return cmd