class HandlerGET:
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, request):
        m = request.get("method", "GET")
        if m == "GET":
            return self.__getattribute__(m.lower())(self.__fn, m)

    def get(self, func, request):
        return f"{request}: {func(request)}"