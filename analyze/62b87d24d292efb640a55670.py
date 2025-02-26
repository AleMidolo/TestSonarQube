def get_versions():
    """
    Get version information or return default if unable to do so.
    """
    import pkg_resources

    try:
        versions = {pkg.project_name: pkg.version for pkg in pkg_resources.working_set}
        return versions
    except Exception:
        return {"default": "unknown"}