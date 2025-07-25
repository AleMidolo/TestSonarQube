def subclasses(cls):
    """
    किसी क्लास के सभी सबक्लासेस को पुनरावृत्त रूप से (recursively) प्राप्त करें।
    """
    subs = cls.__subclasses__()
    for sub in cls.__subclasses__():
        subs.extend(subclasses(sub))
    return subs