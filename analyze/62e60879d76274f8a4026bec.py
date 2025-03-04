def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None, db=None, imp_user=None, dehydration_hooks=None, hydration_hooks=None, **handlers):
    # Set default mode to WRITE if not specified
    if mode is None:
        mode = "WRITE"
    elif mode not in ("READ", "WRITE"):
        raise ValueError("Mode must be either 'READ' or 'WRITE'")

    # Initialize parameters dictionary
    parameters = {}
    
    # Add bookmarks if provided
    if bookmarks:
        parameters["bookmarks"] = list(bookmarks)
        
    # Add metadata if provided
    if metadata:
        parameters["metadata"] = metadata
        
    # Add timeout if provided
    if timeout is not None:
        parameters["timeout"] = timeout
        
    # Add database name if provided (Bolt 4.0+)
    if db is not None:
        parameters["db"] = db
        
    # Add impersonated user if provided (Bolt 4.4+)
    if imp_user is not None:
        parameters["imp_user"] = imp_user

    # Create transaction context with hooks
    tx_context = {
        "mode": mode,
        "parameters": parameters
    }
    
    if dehydration_hooks:
        tx_context["dehydration_hooks"] = dehydration_hooks
    if hydration_hooks:
        tx_context["hydration_hooks"] = hydration_hooks

    # Create and return Response object with handlers
    response = Response(tx_context)
    for key, handler in handlers.items():
        response.add_handler(key, handler)
        
    return response