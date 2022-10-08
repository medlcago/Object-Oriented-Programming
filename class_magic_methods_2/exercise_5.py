class RenderList:
    def __init__(self, type_list: str):
        self.type_list = type_list

    def __call__(self, lst: list):
        if self.type_list not in ("ul", "ol"):
            self.type_list = "ul"
        tags_li = "\n".join(["<li>" + x + "</li>" for x in lst])
        return f'<{self.type_list}>\n{tags_li}\n</{self.type_list}>'