class Book:
    def __init__(self, title: str = "", author: str = "", pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if isinstance(value, Book.__init__.__annotations__.get(key)):
            return super().__setattr__(key, value)
        raise TypeError("Неверный тип присваиваемых данных.")


if __name__ == '__main__':
    book = Book("Python ООП", "Сергей Балакирев", 123, 2022)