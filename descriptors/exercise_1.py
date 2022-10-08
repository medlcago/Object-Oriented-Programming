class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if isinstance(value, float):
            setattr(instance, self.name, value)
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(float(i + 1 + j * M)) for i in range(M)] for j in range(N)]


if __name__ == '__main__':
    table = TableSheet(5, 3)