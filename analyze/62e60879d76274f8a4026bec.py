def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None, db=None, imp_user=None, dehydration_hooks=None, hydration_hooks=None, **handlers):
    # Set default mode to "WRITE" if not specified
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
        
    # Add database name if provided
    if db is not None:
        parameters["db"] = db
        
    # Add impersonated user if provided
    if imp_user is not None:
        parameters["imp_user"] = imp_user

    # Set up dehydration hooks
    if dehydration_hooks:
        self._dehydration_hooks = dehydration_hooks
    else:
        self._dehydration_hooks = {}

    # Set up hydration hooks
    if hydration_hooks:
        self._hydration_hooks = hydration_hooks
    else:
        self._hydration_hooks = {}

    # Create BEGIN transaction message
    message = {
        "mode": mode,
        "parameters": parameters
    }

    # Create and return Response object with handlers
    response = Response(message=message, 
                       dehydration_hooks=self._dehydration_hooks,
                       hydration_hooks=self._hydration_hooks)
    
    # Add any custom handlers
    for key, handler in handlers.items():
        response.add_handler(key, handler)

    return response