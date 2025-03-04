def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Ensure that sender and entity handles match.

    Basically we've already verified the sender is who they say when receiving the payload. However, the sender might
    be trying to set another author in the payload itself, since Diaspora has the sender in both the payload headers
    AND the object. We must ensure they're the same.
    """
    if not sender_handle or not entity_handle:
        return False
        
    # Normalize handles by converting to lowercase and stripping whitespace
    sender = sender_handle.lower().strip()
    entity = entity_handle.lower().strip()
    
    # Check if handles match exactly
    return sender == entity