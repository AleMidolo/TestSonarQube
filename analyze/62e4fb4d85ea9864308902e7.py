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
                # Aggiungi python come interprete
                return (sys.executable,) + cmd
            elif ext == '.sh':
                # Aggiungi bash come interprete
                bash_path = 'C:\\Program Files\\Git\\bin\\bash.exe'
                if os.path.exists(bash_path):
                    return (bash_path,) + cmd
                
    return cmd