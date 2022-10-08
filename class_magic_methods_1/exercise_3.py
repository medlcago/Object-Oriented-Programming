class LessonItem:
    attrs = {"title": str, "practices": int, "duration": int}

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.attrs:
            if not isinstance(value, self.attrs.get(key)):
                raise TypeError("Неверный тип присваиваемых данных.")
            if key in ("practices", "duration") and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        raise AttributeError(f"Атрибут {item} удалять запрещено.")


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, index):
        self.lessons.pop(index)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, index):
        self.modules.pop(index)