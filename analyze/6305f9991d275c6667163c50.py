def set_cut_chars(self, before: bytes, after: bytes) -> None:
    """
    स्लाइस पॉइंट्स को सीमांकित (delimit) करने के लिए उपयोग किए जाने वाले बाइट्स सेट करें।

    आर्ग्युमेंट्स (Args):
        before: इन डिलीमीटर (delimiters) से पहले फाइल को विभाजित (split) करें।
        after: इन डिलीमीटर (delimiters) के बाद फाइल को विभाजित (split) करें।
    """
    self.before_cut_chars = before
    self.after_cut_chars = after