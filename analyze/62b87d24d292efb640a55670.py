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

        # Get versions of installed packages
        for dist in importlib.metadata.distributions():
            versions["packages"][dist.metadata["Name"]] = dist.version

        return versions
    except Exception:
        return {"python": "unknown", "platform": "unknown", "packages": {}}