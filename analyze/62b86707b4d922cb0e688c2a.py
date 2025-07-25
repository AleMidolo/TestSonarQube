def on(self, hook):
    """
    रजिस्ट्री में एक नया हैंडलर जोड़ने के लिए डेकोरेटर फ़ंक्शन।

    पैरामीटर (Args):
    - hook (HookType): वह हुक विशेषता जिसके लिए हैंडलर को पंजीकृत (register) करना है।

    रिटर्न (Returns):
    - callable: निर्दिष्ट हुक के लिए श्रोताओं (listeners) को पंजीकृत करने के लिए डेकोरेटर।
    """
    def decorator(handler):
        if hook not in self.registry:
            self.registry[hook] = []
        self.registry[hook].append(handler)
        return handler
    return decorator