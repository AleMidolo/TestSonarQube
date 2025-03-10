import os

def inject_config(self):
    """
    Establece la variable de entorno para la ruta de configuración si no está definida.
    """
    config_path = os.getenv('CONFIG_PATH')
    if config_path is None:
        os.environ['CONFIG_PATH'] = '/ruta/por/defecto/config'