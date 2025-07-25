def on(self, hook):
    """
    रजिस्ट्री में एक नया हैंडलर जोड़ने के लिए डेकोरेटर फ़ंक्शन।

    पैरामीटर (Args):
    - hook (HookType): वह हुक विशेषता जिसके लिए हैंडलर को पंजीकृत (register) करना है।

    रिटर्न (Returns):
    - callable: निर्दिष्ट हुक के लिए श्रोताओं (listeners) को पंजीकृत करने के लिए डेकोरेटर।
    """
    def decorator(func):
        if not hasattr(self, '_handlers'):
            self._handlers = {}
        if hook not in self._handlers:
            self._handlers[hook] = []
        self._handlers[hook].append(func)
        return func
    return decorator