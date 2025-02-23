def aggiungi_ignorati(ignorati):
    """
    Utilizza il comando git per ottenere i nomi dei file, trasformali in una lista, ordina la lista per includere solo i file ignorati, restituisci quei file come una singola stringa con ogni nome di file separato da una virgola.
    """
    import subprocess

    # Esegui il comando git per ottenere i file ignorati
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    
    # Ottieni l'output e trasformalo in una lista di file
    file_list = result.stdout.strip().split('\n')
    
    # Filtra i file ignorati
    ignored_files = [line.split(':')[1].strip() for line in file_list if line]
    
    # Ordina i file ignorati
    ignored_files.sort()
    
    # Restituisci i file come una stringa separata da virgole
    return ', '.join(ignored_files)