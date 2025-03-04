def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # Si no se proporcionan raíces, inicializar conjunto vacío
    if roots is None:
        roots = set()
    
    # Obtener todos los sujetos y objetos que participan en la propiedad
    subjects = set(graph.subjects(prop))
    objects = set(graph.objects(prop))
    
    # Las raíces son los objetos que no aparecen como sujetos
    # Es decir, los nodos que no tienen padres
    roots.update(objects - subjects)
    
    # Si no hay raíces explícitas, los nodos sin padres son raíces
    if not roots:
        roots.update(subjects - objects)
    
    # Si aún no hay raíces, todos los nodos son raíces
    if not roots:
        roots.update(subjects)
        roots.update(objects)
        
    return roots