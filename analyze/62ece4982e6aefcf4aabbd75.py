def aggiungi_ignorati(ignorati):
    """
    Utilizza il comando git per ottenere i nomi dei file, trasformali in una lista, ordina la lista per includere solo i file ignorati, restituisci quei file come una singola stringa con ogni nome di file separato da una virgola.
    """
    import subprocess

    # Esegui il comando git per ottenere i file ignorati
    result = subprocess.run(['git', 'check-ignore', '-v', '*'], stdout=subprocess.PIPE, text=True)
    
    # Estrai i nomi dei file dalla output
    file_lines = result.stdout.strip().split('\n')
    ignored_files = [line.split(': ')[-1] for line in file_lines if line]

    # Ordina i file ignorati
    ignored_files.sort()

    # Restituisci i file come una stringa separata da virgole
    return ', '.join(ignored_files)