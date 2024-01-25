#!/usr/bin/env python3
import cmd
import sys

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "
    def emptyline(self):
        """Called when an empty line is entered."""
        print("do line")

    def do_help(self, arg):
        if not sys.stdin.isatty():
            print()
        super().do_help()

    def do_quit(self, arg):
        """ Exit the console."""
        return True

    def do_EOF(self, arg):
        """ Exit on Ctrl-D """
        print()
        return True

    def postcmd(self, stop, line):
        """Called after a command is executed."""
        return stop

if __name__ == '__main__':
    console = MyConsole()
    console.cmdloop()
