#!/usr/bin/python3
"""Defines the module ``console`` that
   contains ``HBNBCommand`` that inherit from
   python's ``cmd`` model.
"""
import cmd
from models.base_model import BaseModel 
from models import storage

#print(BaseModel())
#print(storage.all())


class HBNBCommand(cmd.Cmd):
    """Defines an new ``HBNBComand`` class.
       which is the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        print("Quit command to exit the program. \n")

    def do_EOF(self, line):
        """End of file handling"""
        return self.do_quit(line)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it 
           (to the JSON file) and prints the id. Ex: $ create BaseModel

          Prints:
           ** class name missing **: If the class name is missing
           ** class doesn't exist **: If the class name doesn’t exis
        """
        list = line.split()
        if len(list) == 0:
             print(self.error_msg(0))
             return
        elif len(list) == 1 and list[0] != "BaseModel":
            print(self.error_msg(1))
            return
        else:
            my_model = BaseModel()
            print(my_model.id)

    def help_create(self):
        print("Creates a new instance of BaseModel class. \n")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def error_msg(self, param):
        """Error massage handling"""
        switcher = {
            0: "** class name missing **",
            1: "** class doesn't exist **",
            2: "** instance id missing **",
        }

        return switcher[param]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
