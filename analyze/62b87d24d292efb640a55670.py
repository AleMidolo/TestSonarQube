def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        import pkg_resources
        import platform
        import sys
        
        versions = {
            'python': sys.version.split()[0],
            'platform': platform.platform(),
            'pkg_resources': pkg_resources.__version__
        }
        
        return versions
        
    except Exception:
        # Return default version info if unable to get actual versions
        return {
            'python': 'unknown',
            'platform': 'unknown',
            'pkg_resources': 'unknown'
        }