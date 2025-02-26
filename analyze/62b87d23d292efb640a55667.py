def register_vcs_handler(vcs, method): # 装饰器
  """
  创建一个装饰器，用于将方法标记为对象的处理器。
  创建一个装饰器，用于将方法标记为某个版本控制系统（VCS）的处理器。
  """
  def decorate(f):
    """
    创建一个装饰器，用于将方法标记为某个版本控制系统（VCS）的处理器。
    """
    if not hasattr(decorate, 'handlers'):
        decorate.handlers = {}
    if vcs not in decorate.handlers:
        decorate.handlers[vcs] = {}
    decorate.handlers[vcs][method] = f
    return f
  return decorate