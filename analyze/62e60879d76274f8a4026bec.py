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

    # Create message with BEGIN command and parameters
    message = {
        "type": "BEGIN",
        "parameters": parameters
    }

    # Set hooks if provided
    if dehydration_hooks:
        message["dehydration_hooks"] = dehydration_hooks
    if hydration_hooks:
        message["hydration_hooks"] = hydration_hooks

    # Add message to output queue
    self._append(message, **handlers)

    # Return Response object
    return Response(self, **handlers)