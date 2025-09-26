class BitStatusUtil:
    _MIN_VALUE = 0

    @staticmethod
    def add(states, stat):
        BitStatusUtil.check(states, stat)
        return states | stat

    @staticmethod
    def has(states, stat):
        BitStatusUtil.check(states, stat)
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        BitStatusUtil.check(states, stat)
        if BitStatusUtil.has(states, stat):
            return states ^ stat
        return states

    @staticmethod
    def check(*args):
        for arg in args:
            BitStatusUtil.validate(arg)

    @staticmethod
    def validate(arg):
        if arg < BitStatusUtil._MIN_VALUE:
            raise ValueError(f"{arg} must be greater than or equal to {BitStatusUtil._MIN_VALUE}")
        if arg % 2 != 0:
            raise ValueError(f"{arg} not even")