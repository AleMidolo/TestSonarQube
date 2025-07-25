class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        BitStatusUtil.validate_states(states, stat)
        return states | stat

    @staticmethod
    def has(states, stat):
        BitStatusUtil.validate_states(states, stat)
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        BitStatusUtil.validate_states(states, stat)
        if BitStatusUtil.has(states, stat):
            return states ^ stat
        return states

    @staticmethod
    def validate_states(*args):
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} must be greater than or equal to 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")