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
        """
        quit command exits the program
        """
        raise SystemExit

    def do_EOF(self, arg):
        """
        Exits the application on End of File
        """
        raise SystemExit

    def emptyline(self):
        """
        When empty line, do nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        Saves new instance to the JSON file
        Prints the id of the new instance

        If the class name is missing, prints:
            ** class name missing **

        If the class name doesn't exist, prints:
            ** class doesn't exist **
        """
        pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id

        If the class name is missing, prints:
            ** class name missing **

        If the class name doesn't exist, prints:
            ** class doesn't exist **

        If the id is missing, prints:
            ** instance id missing **

        If the instance of the class name doesn't exist for the id, prints:
            ** no instance found **
        """
        pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        and saves change to the JSON file

        If the class name is missing, prints:
            ** class name missing **

        If the class name doesn't exist, prints:
            ** class doesn't exist **

        If the id is missing, prints:
            ** instance id missing **

        If the instance of the class name doesn't exist for the id, print:
            ** no instance found **
        """
        pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.

        The printed result will be a list of strings
        If the class name doesn't exist, prints:
            ** class doesn't exist **
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute(saved to the JSON file)
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
