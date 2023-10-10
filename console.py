#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program at end of file (Ctrl-D)
        """
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
