#!/usr/bin/python3
class MagicClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = 0

    def calculate(self):
        for n in range(1, 3):
            try:
                if n > self.a:
                    raise Exception("Too far")
                self.sum += (self.a ** self.b) / n
            except Exception:
                self.sum = self.b + self.a
                break

        return self.sum
