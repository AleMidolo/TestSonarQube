def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None, db=None, imp_user=None, dehydration_hooks=None, hydration_hooks=None, **handlers):
    # Set default mode to WRITE if not specified
    if mode is None:
        mode = "WRITE"
    elif mode not in ("READ", "WRITE"):
        raise ValueError("Mode must be either 'READ' or 'WRITE'")

    # Initialize parameters dictionary
    parameters = {}
    
    # Add optional parameters if provided
    if bookmarks:
        parameters["bookmarks"] = list(bookmarks)
    if metadata:
        parameters["metadata"] = metadata
    if timeout is not None:
        parameters["timeout"] = timeout
    if db:
        parameters["db"] = db
    if imp_user:
        parameters["imp_user"] = imp_user
        
    # Set up hooks
    if dehydration_hooks:
        self._dehydration_hooks = dehydration_hooks
    if hydration_hooks:
        self._hydration_hooks = hydration_hooks

    # Create and send BEGIN message
    message = {
        "mode": mode,
        "parameters": parameters
    }
    
    # Create Response object with provided handlers
    response = Response(**handlers)
    
    # Send BEGIN message and return response
    self._connection.write_message(("BEGIN", message))
    return response