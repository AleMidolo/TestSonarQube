def inject_config(self):
    """
    Establece la variable de entorno para la ruta de configuración si no está definida.
    """
    import os
    
    if 'CONFIG_PATH' not in os.environ:
        default_config_path = os.path.join(os.path.dirname(__file__), 'config')
        os.environ['CONFIG_PATH'] = default_config_path