def get_versions():
    """
    Obtén la información de la versión o devuelve el valor predeterminado si no es posible obtenerla.
    """
    try:
        import pkg_resources
        version_info = pkg_resources.get_distribution("your_package_name").version
        return version_info
    except Exception:
        return "Versión no disponible"