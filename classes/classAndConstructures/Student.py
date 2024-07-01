class Study:
    # name = ""
    # age = ""

    def __init__(self, fname=None, fage=None):
        self.name = fname
        self.age = fage
        # print(name, age)


    def chanhenameandage(self, fname, fage):
        self.name = fname
        self.age = fage

    def printd(self):
        print(self.name, self.age)


stu = Study()
stu.printd()
stu.chanhenameandage("ram", 33)
stu.printd()
st = Study()
