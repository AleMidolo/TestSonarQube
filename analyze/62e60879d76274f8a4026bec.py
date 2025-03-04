def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
              db=None, imp_user=None, dehydration_hooks=None,
              hydration_hooks=None, **handlers):
    
    # Set default mode to WRITE if not specified
    if mode is None:
        mode = "WRITE"
    
    # Validate mode
    if mode not in ("READ", "WRITE"):
        raise ValueError("Mode must be either 'READ' or 'WRITE'")

    # Initialize parameters dict
    parameters = {}
    
    # Add mode
    parameters["mode"] = mode
    
    # Add bookmarks if provided
    if bookmarks:
        parameters["bookmarks"] = list(bookmarks)
        
    # Add metadata if provided
    if metadata:
        parameters["metadata"] = metadata
        
    # Add timeout if provided
    if timeout is not None:
        parameters["timeout"] = timeout
        
    # Add database if provided
    if db is not None:
        parameters["db"] = db
        
    # Add impersonated user if provided
    if imp_user is not None:
        parameters["imp_user"] = imp_user
        
    # Add dehydration hooks if provided
    if dehydration_hooks is not None:
        parameters["dehydration_hooks"] = dehydration_hooks
        
    # Add hydration hooks if provided 
    if hydration_hooks is not None:
        parameters["hydration_hooks"] = hydration_hooks

    # Create BEGIN message
    message = {
        "type": "BEGIN",
        "parameters": parameters
    }
    
    # Add message to output queue
    self._append(message, **handlers)
    
    # Return Response object
    return Response(self, **handlers)