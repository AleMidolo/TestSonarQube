def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Restituisce i nomi e le descrizioni degli attributi definiti dall'interfaccia."""
    if not all:
        return [(name, attr.getDoc()) 
                for name, attr in self.namesAndDescriptions(all=True)
                if not name.startswith('_')]
    
    return [(name, attr.getDoc()) 
            for name, attr in self.getDescriptors() 
            if IElement.providedBy(attr)]