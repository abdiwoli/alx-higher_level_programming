#!/usr/bin/python3
"""class lock"""

class LockedClass:
    """ class lock """


    def __setattr__(self, name, value):
        if hasattr(self, name) or name == "first_name":
            super().__setattr__(name, value)
        else:
            s = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(s)
