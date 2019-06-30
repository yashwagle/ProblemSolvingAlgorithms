
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currenttask = None
        self.timeremaining = 0

    def