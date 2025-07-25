def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        import sys
        import platform
        import importlib.metadata

        python_version = sys.version.split()[0]
        os_info = platform.platform()
        try:
            package_version = importlib.metadata.version('your_package_name')
        except importlib.metadata.PackageNotFoundError:
            package_version = "unknown"

        return {
            "python_version": python_version,
            "os_info": os_info,
            "package_version": package_version
        }
    except Exception:
        return {
            "python_version": "unknown",
            "os_info": "unknown",
            "package_version": "unknown"
        }