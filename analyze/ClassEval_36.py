from datetime import datetime

class EmailClient:
    def __init__(self, addr, capacity) -> None:
        self.addr = addr
        self.capacity = capacity
        self.inbox = []
    
    def send_to(self, recv, content, size):
        if not recv.is_full_with_one_more_email(size):
            email = self.create_email(recv, content, size)
            recv.inbox.append(email)
            return True
        else:
            self.clear_inbox(size)
            return False
    
    def create_email(self, recv, content, size):
        timestamp = self.get_current_timestamp()
        return {
            "sender": self.addr,
            "receiver": recv.addr,
            "content": content,
            "size": size,
            "time": timestamp,
            "state": "unread"
        }

    def get_current_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def fetch(self):
        unread_email = self.get_unread_email()
        if unread_email:
            unread_email['state'] = "read"
            return unread_email
        return None

    def get_unread_email(self):
        for email in self.inbox:
            if email['state'] == "unread":
                return email
        return None

    def is_full_with_one_more_email(self, size):
        return self.get_occupied_size() + size > self.capacity
        
    def get_occupied_size(self):
        return sum(email["size"] for email in self.inbox)

    def clear_inbox(self, size):
        if not self.addr:
            return
        freed_space = 0
        while freed_space < size and self.inbox:
            email = self.inbox[0]
            freed_space += email['size']
            del self.inbox[0]