def get_versions():
    import platform
    
    try:
        version_info = platform.version()
        return version_info
    except Exception:
        return "default_version"