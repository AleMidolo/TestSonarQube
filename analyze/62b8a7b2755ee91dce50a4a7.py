from datetime import datetime

def default_tzinfo(dt, tzinfo):
    """
    केवल उन naive datetime पर ``tzinfo`` पैरामीटर सेट करता है।

    यह उपयोगी है, उदाहरण के लिए, जब आपको एक datetime प्रदान किया जाता है 
    जिसमें या तो एक implicit या explicit time zone हो सकता है, जैसे कि 
    जब आप एक time zone string को पार्स कर रहे हों।

    :param dt:
        वह datetime जिस पर time zone को बदलना है।

    :param tzinfo:
        :py:class:`datetime.tzinfo` सबक्लास का उदाहरण, जिसे ``dt`` पर 
        असाइन किया जाएगा यदि (और केवल यदि) यह naive है।

    :return:
        एक aware :py:class:`datetime.datetime` लौटाता है।
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tzinfo)
    return dt