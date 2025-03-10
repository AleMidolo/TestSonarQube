import os

def inject_config(self):
    """
    Establece la variable de entorno para la ruta de configuración si no está definida.
    """
    config_path = "/ruta/de/configuracion"  # Cambia esto por la ruta deseada
    if "CONFIG_PATH" not in os.environ:
        os.environ["CONFIG_PATH"] = config_path