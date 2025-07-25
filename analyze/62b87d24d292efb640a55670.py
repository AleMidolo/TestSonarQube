def get_versions():
    """
    Ottieni le informazioni sulla versione o restituisci il valore predefinito se non è possibile ottenerle.
    """
    try:
        import sys
        import platform
        import django
        
        versions = {
            'python': sys.version.split()[0],
            'platform': platform.platform(),
            'django': django.get_version()
        }
        
        return versions
        
    except Exception:
        # Return default values if unable to get version info
        return {
            'python': 'unknown',
            'platform': 'unknown', 
            'django': 'unknown'
        }