def render(pieces, style):
    """
    将输入的组件和样式渲染为对应的样式。
    将给定的组件渲染为要求的样式。
    """
    rendered_output = []
    for piece in pieces:
        rendered_piece = f"<div class='{style}'>{piece}</div>"
        rendered_output.append(rendered_piece)
    return ''.join(rendered_output)