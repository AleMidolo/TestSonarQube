def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
          db=None, imp_user=None, dehydration_hooks=None,
          hydration_hooks=None, **handlers):
    """
    Adds a BEGIN message to the output queue.

    :param mode: Access mode for routing - "READ" or "WRITE" (default)
    :param bookmarks: Iterable of bookmark values that this transaction should follow
    :param metadata: Custom metadata dictionary to attach to the transaction
    :param timeout: Timeout for transaction execution (in seconds)
    :param db: Name of the database against which to start the transaction
        Requires Bolt 4.0+.
    :param imp_user: User to impersonate
        Requires Bolt 4.4+.
    :param dehydration_hooks:
        Hooks to dehydrate types (dict mapping type (class) to dehydration
        function). Dehydration function receives a value and returns an object
        of a type understood by packstream.
    :param hydration_hooks:
        Hooks to hydrate types (dict mapping type (class) to hydration
        function). Hydration function receives a value of a type understood by
        packstream and is free to return anything.
    :param handlers: Handler functions that are passed to the returned Response object
    :return: Response object
    """
    # Create the BEGIN message
    begin_message = {
        "mode": mode,
        "bookmarks": bookmarks,
        "metadata": metadata,
        "timeout": timeout,
        "db": db,
        "imp_user": imp_user,
        "dehydration_hooks": dehydration_hooks,
        "hydration_hooks": hydration_hooks,
        **handlers
    }

    # Add the BEGIN message to the output queue
    self.output_queue.append(begin_message)

    # Return a Response object
    return Response(begin_message)