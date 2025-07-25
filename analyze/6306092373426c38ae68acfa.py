def get_spec_defaults(self):
    """
    Resolver los valores de los argumentos desde la especificación y otras fuentes.
    """
    defaults = {}
    
    if hasattr(self, 'spec') and self.spec:
        # Obtener valores por defecto de la especificación
        for param_name, param in self.spec.parameters.items():
            if hasattr(param, 'default'):
                defaults[param_name] = param.default
                
        # Obtener valores de la configuración global si existe
        if hasattr(self, 'config') and self.config:
            for key, value in self.config.items():
                if key in self.spec.parameters:
                    defaults[key] = value
                    
        # Obtener valores de variables de entorno
        for param_name in self.spec.parameters:
            env_value = os.environ.get(param_name.upper())
            if env_value is not None:
                defaults[param_name] = env_value
                
    return defaults