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
             print("** class name missing **")
             return
        elif len(list) == 1 and list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def help_create(self):
        print("Creates a new instance of BaseModel class. \n")

    def do_show(self, line):
        """ Prints the string representation of an instance based
            on the class name and id. Ex: $ show BaseModel 1234-1234-1234

           Prints:
             ** class name missing **: If the class name is missing,
             ** class doesn't exist **: If the class name doesn’t exist,
             ** instance id missing **: If the instance of the class name
                  doesn’t exist for the id
             ** no instance found **: If the instance of the class name doesn’t
                  exist for the id
        """
        list = line.split()
        if len(list) == 0:
             print("** class name missing **")
             return
        if len(list) == 1:
            print("** instance id missing **")
            return
        if len(list) == 2 and list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(list) == 2 and list[0] == "BaseModel":
            key = f"{list[0]}.{list[1]}"
            objects = storage.all()
            if key in objects.keys():
                #dict = objects[key]
                obj = BaseModel(**objects[key])
                print(obj)
            else:
                print("** instance id missing **")

    def help_show(self):
        print("""Prints the string representation of an instance based on
the class name and id ( ex: BaseModel 1234-1234-1234)\n""")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
           (save the change into the JSON file). 
           Ex: $ destroy BaseModel 1234-1234-1234

        Prints:
          ** class name missing **: If the class name is missing
          ** class doesn't exist **: If the class name doesn’t exist
          ** instance id missing **: If the id is missing
          ** no instance found **: If the instance of the class name
             doesn’t exist for the id\n
        """
        list = line.split()
        if len(list) == 0:
             print("** class name missing **")
             return
        if len(list) == 1:
            print("** instance id missing **")
            return
        if len(list) == 2 and list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(list) == 2 and list[0] == "BaseModel":
            key = f"{list[0]}.{list[1]}"
            objects = storage.all()
            if key in objects.keys():
                del objects[key]
                storage.save()
            else:
                print("** instance id missing **")

    def help_destroy(self):
        print("""Deletes an instance based on the class name and id
(save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.""")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the 
           class name. Ex: $ all BaseModel or $ all.
        Role:
            ** class doesn't exist **: If the class name doesn’t exist,
        """
        list = line.split()
        if len(list) and list[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        objs = storage.all()
        str_list = []
        for key in objs.keys():
            obj = BaseModel(**objs[key])
            str_list.append(str(obj))
        print(str_list)

    def help_all(self):
        print("Prints a list of string representation of all instances")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
