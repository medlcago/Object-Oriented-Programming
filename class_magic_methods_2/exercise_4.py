class DigitRetrieve:
    def __call__(self, num: str):
        try:
            return int(num)
        except ValueError:
            return None