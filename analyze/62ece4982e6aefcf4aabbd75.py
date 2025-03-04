def addignored(ignored):
    """
    Utilizza il comando git per ottenere i nomi dei file, trasformali in una lista, ordina la lista per includere solo i file ignorati, restituisci quei file come una singola stringa con ogni nome di file separato da una virgola.
    """
    import subprocess

    # Esegui il comando git per ottenere i file ignorati
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    
    # Ottieni l'output e trasformalo in una lista di file
    ignored_files = result.stdout.strip().split('\n')
    
    # Ordina la lista di file ignorati
    ignored_files = sorted(set(file.split(':')[1].strip() for file in ignored_files if file))
    
    # Restituisci i file come una singola stringa separata da virgole
    return ', '.join(ignored_files)