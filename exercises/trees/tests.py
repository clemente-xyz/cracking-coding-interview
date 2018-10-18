class Test():
    def __init__(self):
        self.data = 3

    def show(self):
        show_me(self.data)


def show_me(data):
    print(data)


test = Test()

test.show()
