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
            'packages': {}
        }
        
        # Get installed package versions
        installed_packages = pkg_resources.working_set
        for package in installed_packages:
            versions['packages'][package.key] = package.version
            
        return versions
        
    except Exception:
        # Return default version info if unable to get actual versions
        return {
            'python': 'unknown',
            'platform': 'unknown',
            'packages': {}
        }