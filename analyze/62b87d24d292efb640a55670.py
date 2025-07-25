def get_versions():
    """
    Ottieni le informazioni sulla versione o restituisci il valore predefinito se non è possibile ottenerle.
    """
    try:
        import sys
        import platform
        
        versions = {
            'python': sys.version.split()[0],
            'platform': platform.platform(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'system': platform.system(),
            'release': platform.release()
        }
        
        return versions
        
    except Exception:
        # Return default values if version info cannot be obtained
        return {
            'python': 'unknown',
            'platform': 'unknown',
            'machine': 'unknown', 
            'processor': 'unknown',
            'system': 'unknown',
            'release': 'unknown'
        }