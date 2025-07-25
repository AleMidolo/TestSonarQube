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
        
    # Add database name if provided (Bolt 4.0+)
    if db is not None:
        parameters["db"] = db
        
    # Add impersonated user if provided (Bolt 4.4+)
    if imp_user is not None:
        parameters["imp_user"] = imp_user

    # Create transaction configuration
    tx_config = {
        "mode": mode,
        "parameters": parameters
    }

    # Set up dehydration hooks
    if dehydration_hooks:
        self._dehydration_hooks = dehydration_hooks
    
    # Set up hydration hooks
    if hydration_hooks:
        self._hydration_hooks = hydration_hooks

    # Begin transaction and create Response object
    try:
        self._connection.begin(tx_config)
        response = Response(self._connection, **handlers)
        return response
    except Exception as e:
        # Clean up hooks if set
        if dehydration_hooks:
            self._dehydration_hooks = None
        if hydration_hooks:
            self._hydration_hooks = None
        raise e