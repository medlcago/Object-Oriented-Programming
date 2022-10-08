class InputDigits:
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        return list(map(int, self.__fn().split()))


input_dg = InputDigits(input)
res = input_dg()