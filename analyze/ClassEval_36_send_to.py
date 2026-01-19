def send_to(self, recv, content, size):
    """
    दिए गए ईमेल पते पर एक ईमेल भेजता है।
    :param recv: रिसीवर का ईमेल पता, str.
    :param content: ईमेल की सामग्री, str.
    :param size: ईमेल का आकार, float.
    :return: यदि ईमेल सफलतापूर्वक भेजा गया है तो True, यदि रिसीवर का ईमेल बॉक्स भरा हुआ है तो False.
    """
    from datetime import datetime
    
    # Check if receiver has enough space in their inbox
    if recv.get_occupied_size() + size > recv.capacity:
        return False
    
    # Create email object
    email = {
        'sender': self.email,
        'receiver': recv.email,
        'content': content,
        'size': size,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'unread'
    }
    
    # Add email to receiver's inbox
    recv.inbox.append(email)
    
    return True