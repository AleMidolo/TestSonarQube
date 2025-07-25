def render(pieces, style):
    """
    将输入的组件和样式渲染为对应的样式。
    将给定的组件渲染为要求的样式。
    """
    rendered = []
    
    # 遍历所有组件
    for piece in pieces:
        # 根据样式类型进行渲染
        if style == "bold":
            rendered.append(f"**{piece}**")
        elif style == "italic":
            rendered.append(f"*{piece}*") 
        elif style == "underline":
            rendered.append(f"_{piece}_")
        else:
            # 默认不添加样式
            rendered.append(piece)
            
    # 将渲染后的组件连接起来
    return "".join(rendered)