#!/usr/bin/python3
"""class lock"""

class LockedClass:
    def __setattr__(self, name, value):
        if hasattr(self, name) or name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
