import subprocess

def aggiungi_ignorati(ignorati):
    """
    Utilizza il comando git per ottenere i nomi dei file, trasformali in una lista, ordina la lista per includere solo i file ignorati, restituisci quei file come una singola stringa con ogni nome di file separato da una virgola.
    """
    # Ottieni la lista dei file ignorati da git
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], stdout=subprocess.PIPE)
    ignored_files = result.stdout.decode('utf-8').splitlines()
    
    # Filtra i file ignorati in base alla lista fornita
    filtered_files = [file for file in ignored_files if file in ignorati]
    
    # Ordina la lista dei file ignorati
    filtered_files.sort()
    
    # Restituisci i file come una singola stringa separata da virgole
    return ', '.join(filtered_files)