#!/usr/bin/python3
"""Defines the module ``console`` that
   contains ``HBNBCommand`` that inherit from
   python's ``cmd`` model.
"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
        args = line.split()
        if len(args) == 0:
             print("** class name missing **")
             return
        if args[0] in classes:
            #new_dict = self.input_parcer(args[1:])
            #print(new_dict)
            new = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return
        #print(new)
        print(new.id)
        new.save()

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
        args = line.split()
        if len(args) == 0:
             print("** class name missing **")
             return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) > 1 and args[0] in classes:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            obj = objects[key]
            print(obj)
        else:
            print("** class doesn't exist **")
            return

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
        args = line.split()
        if len(args) == 0:
             print("** class name missing **")
             return
        if len(args) == 1:
            print("** instance id missing **")
            return
        #if len(args) == 2 and classes.get(args[0]) == None:
        if len(args) == 2 and args[0] in classes:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if objects.get(key) == None:
                print("** no instance found **")
                return
            del objects[key]
            storage.save()
        else:
            print("** class doesn't exist **")
            return

    def help_destroy(self):
        print("""Deletes an instance based on the class name and id
(save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.""")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
           to the class name. Ex: $ all BaseModel or $ all.
        Role:
            ** class doesn't exist **: If the class name doesn’t exist,
        """
        list = line.split()
        if len(list) and list[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        obj_list = []
        for k in all_objs:
            obj_list.append(str(all_objs[k]))
        print(obj_list)

    def help_all(self):
        print("Prints a list of string representation of all instances")

    def do_update(self, line):
        """ Updates an instance based on the class name and id.
        (Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com")

         Prints:
           ** class name missing **: If the class name is missing,
           ** class doesn't exist **: If the class name doesn’t exist,
           ** instance id missing **: If the instance of the class name
               doesn’t exist for the id
           ** no instance found **: If the instance of the class name doesn’t
                exist for the id
           ** attribute name missing **: If the attribute name is missing
         ** value missing **: If the value for the attribute name doesn’t exist
        """
        list = line.split()
        if len(list) == 0:
             print("** class name missing **")
             return
        if len(list) == 1:
            print("** instance id missing **")
            return
        if len(list) >= 2 and list[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(list) == 2 and list[0] == "BaseModel":
            print("** attribute name missing **")
            return
        if len(list) == 3 and list[0] == "BaseModel":
            print("** value missing **")
            return
        if len(list) >= 3 and list[0] == "BaseModel":
            key = f"{list[0]}.{list[1]}"
            objects = storage.all()
            if key in objects.keys():
                obj = objects[key]
                obj[list[2]] = list[3]
                storage.save()
                print(obj)
            else:
                print("** no instance found **")

    def help_update(self):
        print("""Updates an instance based on the class name and id.
Usage: update <class name> <id> <attribute name> "<attribute value>\n""")


    def input_parcer(self, args):
        """Returns a dictonary based on argument passed"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

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
