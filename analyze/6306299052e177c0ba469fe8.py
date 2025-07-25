def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    Ensure that sender and entity handles match.

    Basically we've already verified the sender is who they say when receiving the payload. However, the sender might
    be trying to set another author in the payload itself, since Diaspora has the sender in both the payload headers
    AND the object. We must ensure they're the same.

    Args:
        sender_handle (str): The handle of the sender.
        entity_handle (str): The handle of the entity in the payload.

    Returns:
        bool: True if the sender and entity handles match, False otherwise.
    """
    return sender_handle == entity_handle