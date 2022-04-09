class C:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Said' * 3

c = C(40)
print(c)