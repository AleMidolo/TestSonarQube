def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """
    返回当前类属性的名称和描述。
    如果all为假，则返回由接口定义的属性名称和描述。
    """
    if all:
        return {attr: getattr(self, attr).__doc__ for attr in dir(self) if not attr.startswith('__')}
    else:
        return {attr: getattr(self, attr).__doc__ for attr in self.interface_properties() if hasattr(self, attr)}

def interface_properties(self):
    # This method should return a list of property names defined by the interface
    return ['property1', 'property2']  # Example property names