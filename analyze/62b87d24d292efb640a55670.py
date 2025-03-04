def get_versions():
    """
    Obtén la información de la versión o devuelve el valor predeterminado si no es posible obtenerla.
    """
    try:
        import pkg_resources
        import platform
        import sys

        versions = {
            'python': sys.version.split()[0],
            'platform': platform.platform(),
            'packages': {
                pkg.key: pkg.version 
                for pkg in pkg_resources.working_set
            }
        }
        
        return versions
        
    except Exception:
        # Return default version info if unable to get actual versions
        return {
            'python': 'unknown',
            'platform': 'unknown',
            'packages': {}
        }