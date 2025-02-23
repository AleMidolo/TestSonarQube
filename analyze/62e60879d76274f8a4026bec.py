def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
          db=None, imp_user=None, dehydration_hooks=None,
          hydration_hooks=None, **handlers):
    # Create the message to be sent
    message = {
        'action': 'BEGIN',
        'mode': mode or 'WRITE',
        'bookmarks': bookmarks,
        'metadata': metadata,
        'timeout': timeout,
        'db': db,
        'imp_user': imp_user,
        'dehydration_hooks': dehydration_hooks,
        'hydration_hooks': hydration_hooks,
        'handlers': handlers
    }
    
    # Add the message to the output queue
    self.output_queue.append(message)
    
    # Return a response object
    return Response(message)