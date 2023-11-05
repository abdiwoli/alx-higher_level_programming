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

    def __getattr__(self, name):
        if name == "first_name" and name != "__dict__":
            return super().__getattribute__(name)
        s = f"'LockedClass' object has no attribute '{name}'"
        raise AttributeError(s)
