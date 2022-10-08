class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except ValueError:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))

        return wrapper


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)