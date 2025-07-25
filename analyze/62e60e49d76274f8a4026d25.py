def unit_of_work(metadata=None, timeout=None):
    """
    यह फ़ंक्शन ट्रांज़ेक्शन फ़ंक्शन्स के लिए एक डेकोरेटर है, जो यह नियंत्रित करने की अतिरिक्त सुविधा प्रदान करता है कि ट्रांज़ेक्शन कैसे निष्पादित किया जाए।

    उदाहरण के लिए, एक टाइमआउट लागू किया जा सकता है::

    from neo4j import unit_of_work

    @unit_of_work(timeout=100)
    def count_people_tx(tx):
        result = tx.run("MATCH (a:Person) RETURN count(a) AS persons")
        record = result.single()
        return record["persons"]

    :param metadata: 
        मेटाडेटा के साथ एक डिक्शनरी।  
        निर्दिष्ट मेटाडेटा निष्पादित ट्रांज़ेक्शन से जुड़ा होगा और ``dbms.listQueries`` और ``dbms.listTransactions`` प्रक्रियाओं के आउटपुट में दिखाई देगा।  
        यह ``query.log`` में भी लॉग किया जाएगा।  
        यह सुविधा ट्रांज़ेक्शन्स को टैग करना आसान बनाती है और ``dbms.setTXMetaData`` प्रक्रिया के समकक्ष है।  
        प्रक्रिया संदर्भ के लिए देखें: [https://neo4j.com/docs/operations-manual/current/reference/procedures/](https://neo4j.com/docs/operations-manual/current/reference/procedures/)।  
    :type metadata: `dict`

    :param timeout: 
        ट्रांज़ेक्शन का टाइमआउट (सेकंड में)।  
        जो ट्रांज़ेक्शन्स निर्दिष्ट टाइमआउट से अधिक समय तक चलते हैं, उन्हें डेटाबेस द्वारा समाप्त कर दिया जाएगा।  
        यह सुविधा क्वेरी/ट्रांज़ेक्शन निष्पादन समय को सीमित करने की अनुमति देती है।  
        निर्दिष्ट टाइमआउट डेटाबेस में कॉन्फ़िगर किए गए डिफ़ॉल्ट टाइमआउट (``dbms.transaction.timeout`` सेटिंग) को ओवरराइड करता है।  
        मान नकारात्मक अवधि का प्रतिनिधित्व नहीं करना चाहिए।  
        शून्य अवधि (0) ट्रांज़ेक्शन को अनिश्चित काल तक चलने देगी।  
        `None` का उपयोग डेटाबेस में कॉन्फ़िगर किए गए डिफ़ॉल्ट टाइमआउट का उपयोग करेगा।  
    :type timeout: `float` या `:const:None`
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # यहाँ ट्रांज़ेक्शन लॉजिक लागू करें
            # मेटाडेटा और टाइमआउट का उपयोग करें
            return func(*args, **kwargs)
        return wrapper
    return decorator