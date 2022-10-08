class ImageFileAcceptor:
    def __init__(self, extensions: tuple):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        return args[0].split(".")[-1] in self.extensions