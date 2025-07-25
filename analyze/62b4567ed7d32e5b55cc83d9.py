def deep_merge_nodes(nodes):
    result = {}
    
    # Recorrer cada nodo en la lista de entrada
    for key_node, value_node in nodes:
        key = key_node.value
        
        # Si la clave no existe, simplemente agregar el par clave-valor
        if key not in result:
            result[key] = (key_node, value_node)
            continue
            
        # Si la clave existe, necesitamos fusionar los valores
        existing_value = result[key][1]
        
        # Si ambos son MappingNodes, hacer una fusión profunda
        if (isinstance(value_node, type(existing_value)) and 
            hasattr(value_node, 'tag') and
            value_node.tag == 'tag:yaml.org,2002:map' and
            existing_value.tag == 'tag:yaml.org,2002:map'):
            
            # Convertir los nodos existentes a un diccionario para facilitar la búsqueda
            existing_dict = {k.value: v for k, v in existing_value.value}
            new_dict = {k.value: v for k, v in value_node.value}
            
            # Fusionar los diccionarios
            merged_pairs = []
            all_keys = set(existing_dict.keys()) | set(new_dict.keys())
            
            for k in all_keys:
                if k in new_dict:
                    # Encontrar el nodo clave original que corresponde a este valor
                    key_node = next(kn for kn, _ in value_node.value if kn.value == k)
                    merged_pairs.append((key_node, new_dict[k]))
                else:
                    # Encontrar el nodo clave original que corresponde a este valor
                    key_node = next(kn for kn, _ in existing_value.value if kn.value == k)
                    merged_pairs.append((key_node, existing_dict[k]))
            
            # Crear un nuevo MappingNode con los valores fusionados
            merged_value = type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=merged_pairs
            )
            result[key] = (key_node, merged_value)
            
        # Si no son MappingNodes o son de diferente tipo, el último valor prevalece
        else:
            result[key] = (key_node, value_node)
    
    # Convertir el diccionario resultante de vuelta a una lista de tuplas
    return list(result.values())