def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    try:
        import sys
        import platform
        import importlib.metadata

        versions = {
            "python": sys.version,
            "platform": platform.platform(),
            "packages": {}
        }

        # Example: Get version of a commonly used package like 'requests'
        try:
            versions["packages"]["requests"] = importlib.metadata.version("requests")
        except importlib.metadata.PackageNotFoundError:
            versions["packages"]["requests"] = "Not installed"

        return versions
    except Exception as e:
        return {"error": str(e), "default": "Unable to retrieve version information"}