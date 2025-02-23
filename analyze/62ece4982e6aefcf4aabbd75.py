def aggiungi_ignorati(ignorati):
    """
    Utilizza il comando git per ottenere i nomi dei file, trasformali in una lista, ordina la lista per includere solo i file ignorati, restituisci quei file come una singola stringa con ogni nome di file separato da una virgola.
    """
    import subprocess

    # Esegui il comando git per ottenere i file ignorati
    result = subprocess.run(['git', 'ls-files', '--ignored', '--exclude-standard'], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            text=True)

    # Controlla se ci sono errori
    if result.returncode != 0:
        raise Exception("Errore nell'esecuzione del comando git: " + result.stderr)

    # Ottieni l'output e crea una lista di file
    file_list = result.stdout.splitlines()

    # Ordina la lista di file
    file_list.sort()

    # Restituisci i file come una stringa separata da virgole
    return ', '.join(file_list)