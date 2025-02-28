def subclasses(cls):
    """
    किसी क्लास के सभी सबक्लासेस को पुनरावृत्त रूप से (recursively) प्राप्त करें।
    """
    for subclass in cls.__subclasses__():
        yield subclass
        yield from subclasses(subclass)