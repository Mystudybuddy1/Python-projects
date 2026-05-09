class a:
    def __init__(self):
        print("class a constructor")

class b(a):
    def __init__(self):
        super().__init__()
        print("class b constructor")

obj = b()
