def fromutc(self, dt):
    """
    दिए गए टाइमज़ोन में एक टाइमज़ोन-अवेयर डेटटाइम को लेते हुए,
    एक नए टाइमज़ोन में टाइमज़ोन-अवेयर डेटटाइम की गणना करता है।

    चूंकि यह वह समय है जब हमें *पक्का* पता है कि हमारे पास एक 
    अस्पष्टता रहित डेटटाइम ऑब्जेक्ट है, हम इस अवसर का उपयोग यह 
    निर्धारित करने के लिए करते हैं कि क्या डेटटाइम अस्पष्ट है और 
    "फोल्ड" स्थिति में है (उदाहरण के लिए, यदि यह अस्पष्ट डेटटाइम 
    का पहला घटना है, कालानुक्रमिक रूप से)।

    :param dt:
        एक टाइमज़ोन-अवेयर :class:`datetime.datetime` ऑब्जेक्ट।
    """
    if dt.tzinfo is None:
        raise ValueError("dt must be timezone-aware")
    
    # Convert the datetime to UTC
    utc_dt = dt.astimezone(self.utc)
    
    # Calculate the new datetime in the target timezone
    new_dt = utc_dt.astimezone(self)
    
    return new_dt