def generate_default_observer_schema(app):
    """
    Generar el esquema de observador predeterminado para cada recurso de Kubernetes presente en  
    ``spec.manifest`` para el cual no se haya especificado un esquema de observador personalizado.

    Argumentos:
    app(krake.data.kubernetes.Application): La aplicación para la cual se generará un esquema de observador predeterminado.
    """
    default_schema = {}
    
    # Si no hay manifiesto, retornar esquema vacío
    if not app.spec.manifest:
        return default_schema
        
    # Iterar sobre cada recurso en el manifiesto
    for resource in app.spec.manifest:
        # Obtener el tipo y nombre del recurso
        kind = resource.get('kind')
        name = resource.get('metadata', {}).get('name')
        
        # Si el recurso ya tiene un esquema personalizado, omitirlo
        if hasattr(app.spec, 'observer') and app.spec.observer.get(f"{kind.lower()}/{name}"):
            continue
            
        # Generar esquema predeterminado para este recurso
        resource_schema = {
            'conditions': [{
                'type': 'Available',
                'status': 'True'
            }],
            'state': {
                'phase': 'Running'
            }
        }
        
        # Agregar al esquema general usando la convención kind/name
        default_schema[f"{kind.lower()}/{name}"] = resource_schema
        
    return default_schema