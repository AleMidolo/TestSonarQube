def addignored(ignored):
    import subprocess
    
    # Esegui il comando git ls-files per ottenere tutti i file
    git_files = subprocess.check_output(['git', 'ls-files', '--others', '--ignored', '--exclude-standard']).decode('utf-8')
    
    # Converti l'output in una lista di file
    files_list = git_files.strip().split('\n')
    
    # Filtra i file vuoti
    files_list = [f for f in files_list if f]
    
    # Ordina la lista alfabeticamente
    files_list.sort()
    
    # Unisci i nomi dei file con virgole
    ignored_files = ','.join(files_list)
    
    return ignored_files