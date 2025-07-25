def _getTargetClass(self):
    """
    定义此方法以返回当前使用的实现类，并去掉 'Py' 或 'Fallback' 后缀。
    """
    class_name = self.__class__.__name__
    if class_name.endswith('Py'):
        return class_name[:-2]
    elif class_name.endswith('Fallback'):
        return class_name[:-7]
    else:
        return class_name