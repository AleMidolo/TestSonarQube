def solve(self):
    """
    使用 BFS 算法找到从初始状态到目标状态的路径解决方案。
    维护一个名为 open_list 的列表作为队列,并将初始状态添加到该队列中。
    始终访问并弹出索引为 0 的元素,调用 get_possible_moves 方法查找所有可能的方向。
    遍历 possible_moves 列表并调用 move 方法以获取多个新状态,然后将它们添加到队列中。
    重复上述步骤,直到 open_list 为空或状态已更改为目标状态。
    :return path: list of str,目标状态的解决方案。
    >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    >>> eightPuzzle.solve()
    ['right']
    """
    from collections import deque
    
    # 初始化队列,存储 (当前状态, 路径)
    open_list = [(self.state, [])]
    
    # 用于记录已访问的状态,避免重复访问
    visited = set()
    visited.add(self._state_to_tuple(self.state))
    
    while open_list:
        # 弹出队列首元素
        current_state, path = open_list.pop(0)
        
        # 检查是否到达目标状态
        if current_state == self.goal_state:
            return path
        
        # 临时保存当前状态
        original_state = self.state
        self.state = current_state
        
        # 获取所有可能的移动方向
        possible_moves = self.get_possible_moves()
        
        # 遍历所有可能的移动
        for direction in possible_moves:
            # 执行移动获取新状态
            new_state = self.move(direction)
            
            # 将状态转换为可哈希的元组用于检查是否访问过
            state_tuple = self._state_to_tuple(new_state)
            
            # 如果新状态未被访问过,添加到队列
            if state_tuple not in visited:
                visited.add(state_tuple)
                new_path = path + [direction]
                open_list.append((new_state, new_path))
        
        # 恢复原始状态
        self.state = original_state
    
    # 如果队列为空仍未找到解,返回空列表
    return []

def _state_to_tuple(self, state):
    """辅助方法:将二维列表状态转换为元组以便哈希"""
    return tuple(tuple(row) for row in state)