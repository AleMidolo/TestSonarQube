def _generate_cards(self):
    """
        为卡片生成1到9之间的随机数字。
        """
    self.nums = [random.randint(1, 9) for _ in range(4)]