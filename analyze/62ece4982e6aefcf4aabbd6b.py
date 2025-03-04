def subclasses(cls):
    """
    किसी क्लास के सभी सबक्लासेस को पुनरावृत्त रूप से (recursively) प्राप्त करें।
    """
    # Initialize empty set to store all subclasses
    all_subclasses = set()
    
    # Get immediate subclasses
    direct_subclasses = cls.__subclasses__()
    
    # Add immediate subclasses to result set
    all_subclasses.update(direct_subclasses)
    
    # Recursively get subclasses of each direct subclass
    for subclass in direct_subclasses:
        all_subclasses.update(subclasses(subclass))
        
    return all_subclasses