#!/usr/bin/python3
"""
This module contains the entry point for the command
interpreter.
"""
import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """
    This class will implement the HBNB builtin Command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """'quit' command exits the program"""
        raise SystemExit

    def do_EOF(self, arg):
        """Exits the application on End of File"""
        raise SystemExit

    def emptyline(self):
        """When empty line, do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
