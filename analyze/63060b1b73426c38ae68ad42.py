def inject_config(self):
    """
    Establece la variable de entorno para la ruta de configuración si no está definida.
    """
    import os

    config_path = os.getenv('CONFIG_PATH')
    if config_path is None:
        default_path = '/etc/myapp/config'
        os.environ['CONFIG_PATH'] = default_path