def check_sender_and_entity_handle_match(sender_handle, entity_handle):
    """
    सुनिश्चित करें कि सेंडर और एंटिटी हैंडल मेल खाते हैं।

    मूल रूप से, हमने पहले ही यह सत्यापित कर लिया है कि जब पेलोड प्राप्त हो रहा है, तो सेंडर वही है जो वह होने का दावा करता है। हालांकि, सेंडर पेलोड में किसी अन्य लेखक को सेट करने की कोशिश कर सकता है, क्योंकि Diaspora में सेंडर की जानकारी पेलोड हेडर और ऑब्जेक्ट दोनों में होती है। हमें यह सुनिश्चित करना होगा कि ये दोनों समान हैं।
    """
    return sender_handle == entity_handle