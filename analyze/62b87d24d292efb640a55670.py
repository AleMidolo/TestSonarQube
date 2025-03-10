def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        import sys
        import platform
        import importlib.metadata

        python_version = sys.version
        os_info = platform.platform()
        package_versions = {}

        # Get versions of installed packages
        for dist in importlib.metadata.distributions():
            package_versions[dist.metadata['Name']] = dist.version

        return {
            "python_version": python_version,
            "os_info": os_info,
            "package_versions": package_versions
        }
    except Exception:
        return {
            "python_version": "unknown",
            "os_info": "unknown",
            "package_versions": {}
        }