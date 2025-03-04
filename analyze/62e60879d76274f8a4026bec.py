def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None, db=None, imp_user=None, dehydration_hooks=None, hydration_hooks=None, **handlers):
    # Set default mode to "WRITE" if not specified
    if mode is None:
        mode = "WRITE"
    elif mode not in ("READ", "WRITE"):
        raise ValueError("Mode must be either 'READ' or 'WRITE'")

    # Initialize parameters dictionary
    parameters = {}
    
    # Add optional parameters if provided
    if bookmarks is not None:
        parameters["bookmarks"] = list(bookmarks)
    if metadata is not None:
        parameters["metadata"] = metadata
    if timeout is not None:
        parameters["timeout"] = timeout
    if db is not None:
        parameters["db"] = db
    if imp_user is not None:
        parameters["imp_user"] = imp_user
        
    # Set up hooks
    if dehydration_hooks is None:
        dehydration_hooks = {}
    if hydration_hooks is None:
        hydration_hooks = {}
        
    # Create transaction context
    tx_context = {
        "mode": mode,
        "parameters": parameters,
        "dehydration_hooks": dehydration_hooks,
        "hydration_hooks": hydration_hooks
    }
    
    # Create and return Response object with handlers
    response = Response(tx_context)
    for key, handler in handlers.items():
        response.add_handler(key, handler)
        
    return response