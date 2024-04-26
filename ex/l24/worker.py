class Worker:
    greeting = 'Str'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeosie.greeting

class Bourgeosie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gether wealth'
