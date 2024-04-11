class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, x):
        if self.pouch_contents.count(x):
            print(x)
        else:
            self.pouch_contents.append(x)

    def __str__(self):
        if self.pouch_contents == []:
            return "The kangaroo's pouch is empty."
        else:
            return "The Kangaroo's pouch contains {0}".format(self.pouch_contents)


def KangarooTestDriver():
    kangaroo = Kangaroo()
    print(kangaroo)
    kangaroo.put_in_pouch('baby')
    print(kangaroo)
    kangaroo.put_in_pouch('baby2')
    print(kangaroo)
    kangaroo.put_in_pouch('baby')
    print(kangaroo)


KangarooTestDriver()
