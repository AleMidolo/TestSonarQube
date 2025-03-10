import os

def inject_config(self):
    """
    Establece la variable de entorno para la ruta de configuración si no está definida.
    """
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = '/ruta/por/defecto/config.yaml'