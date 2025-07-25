def subclasses(cls):
    """
    किसी क्लास के सभी सबक्लासेस को पुनरावृत्त रूप से (recursively) प्राप्त करें।
    """
    subclasses_list = cls.__subclasses__()
    for subclass in subclasses_list:
        subclasses_list.extend(subclasses(subclass))
    return subclasses_list