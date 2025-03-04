def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
          db=None, imp_user=None, dehydration_hooks=None,
          hydration_hooks=None, **handlers):
    
    # Set default mode to WRITE if not specified
    if mode is None:
        mode = "WRITE"
    
    # Validate mode
    if mode not in ("READ", "WRITE"):
        raise ValueError("Mode must be either 'READ' or 'WRITE'")

    # Build extra parameters dict
    extra = {}
    if bookmarks:
        extra["bookmarks"] = list(bookmarks)
    if metadata:
        extra["metadata"] = metadata
    if timeout is not None:
        extra["timeout"] = timeout
    if db:
        extra["db"] = db
    if imp_user:
        extra["imp_user"] = imp_user
    
    # Add hooks if provided
    if dehydration_hooks:
        extra["dehydration_hooks"] = dehydration_hooks
    if hydration_hooks:
        extra["hydration_hooks"] = hydration_hooks

    # Create BEGIN message
    message = {
        "mode": mode
    }
    if extra:
        message.update(extra)

    # Add message to output queue and create Response
    self._append(("BEGIN", message))
    return Response(self._connection, **handlers)