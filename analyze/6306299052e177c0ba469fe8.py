def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Ensure that sender and entity handles match.

    Basically we've already verified the sender is who they say when receiving the payload. However, the sender might
    be trying to set another author in the payload itself, since Diaspora has the sender in both the payload headers
    AND the object. We must ensure they're the same.
    """
    if not sender_handle or not entity_handle:
        return False
        
    # Strip whitespace and convert to lowercase for comparison
    sender = sender_handle.strip().lower()
    entity = entity_handle.strip().lower()
    
    # Check if handles match exactly
    return sender == entity