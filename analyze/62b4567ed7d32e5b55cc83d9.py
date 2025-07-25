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
            existing_dict = {n[0].value: n[1] for n in existing_value.value}
            
            # Fusionar los nuevos valores
            for sub_key_node, sub_value_node in value_node.value:
                existing_dict[sub_key_node.value] = sub_value_node
                
            # Reconstruir el MappingNode con los valores fusionados
            merged_value = type(value_node)(
                tag='tag:yaml.org,2002:map',
                value=[(k_node, existing_dict[k_node.value]) 
                      for k_node, _ in existing_value.value 
                      if k_node.value in existing_dict]
            )
            
            # Agregar cualquier nueva clave que no existía previamente
            for k_node, v_node in value_node.value:
                if k_node.value not in {n[0].value for n in merged_value.value}:
                    merged_value.value.append((k_node, v_node))
                    
            result[key] = (key_node, merged_value)
            
        # Si no son MappingNodes o son de diferente tipo, el último valor prevalece
        else:
            result[key] = (key_node, value_node)
    
    # Convertir el diccionario resultado de vuelta a una lista de tuplas
    return list(result.values())