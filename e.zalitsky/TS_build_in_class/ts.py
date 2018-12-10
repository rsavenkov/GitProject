class Ts:

    def __init__(self, type, workable):
        self.type = type
        self.workable = True

    def isworkable(self, work):
        self.workable = work

    def worked(self):
        if self.workable:
            return "TS on the run"
        else:
            return "TS not on the run"
