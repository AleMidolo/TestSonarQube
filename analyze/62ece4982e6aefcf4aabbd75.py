import subprocess

def aggiungi_ignorati(ignorati):
    """
    Utilizza il comando git per ottenere i nomi dei file, trasformali in una lista, ordina la lista per includere solo i file ignorati, restituisci quei file come una singola stringa con ogni nome di file separato da una virgola.
    """
    result = subprocess.run(['git', 'check-ignore', '-n', '*'], stdout=subprocess.PIPE, text=True)
    file_list = result.stdout.strip().split('\n')
    ignored_files = [file.split(':')[1].strip() for file in file_list if file]
    ignored_files.sort()
    return ', '.join(ignored_files)