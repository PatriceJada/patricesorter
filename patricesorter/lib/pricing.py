class Price:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return '(First {}, Last {})'.format(self.first, self.last)

    def get_first(self):
        """Return first element"""
        return self.first

    def get_last(self):
        """Return last Element"""
        return self.last()
