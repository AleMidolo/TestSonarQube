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

        # Example: Get version of some common packages
        packages_to_check = ["numpy", "pandas", "requests"]
        for package in packages_to_check:
            try:
                versions["packages"][package] = importlib.metadata.version(package)
            except importlib.metadata.PackageNotFoundError:
                versions["packages"][package] = "Not installed"

        return versions

    except Exception as e:
        # Return default version information if any error occurs
        return {
            "python": "Unknown",
            "platform": "Unknown",
            "packages": {}
        }