#!/usr/bin/python3
"""Module for console.py."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB console."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """Exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

