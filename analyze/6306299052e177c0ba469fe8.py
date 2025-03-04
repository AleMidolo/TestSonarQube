def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    检查 sender_handle 是否与 entity_handle 相同。如果相同，则返回真；否则，返回假。

    确保发送者和 entity_handle 匹配。

    基本上，在接收有效负载时，我们已经验证了发送者的身份是否属实。然而，发送者可能会尝试在有效负载本身中设置另一个作者，因为 Diaspora 在有效负载的头部和对象中都包含了发送者信息。我们必须确保它们是相同的。
    """
    if not sender_handle or not entity_handle:
        return False
        
    # 将两个句柄转换为小写进行比较,避免大小写不一致的问题
    sender_handle = str(sender_handle).lower().strip()
    entity_handle = str(entity_handle).lower().strip()
    
    return sender_handle == entity_handle