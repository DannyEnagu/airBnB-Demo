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

classes = {
            "Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User
          }


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
            # new_dict = self.input_parcer(args[1:])
            new = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return
        # print(new)
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
        if len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
            return
        if len(args) > 1 and args[0] in classes:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if objects.get(key) is None:
                print("** no instance found **")
                return
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
        if len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
            return
        if len(args) == 2 and args[0] in classes:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if objects.get(key) is None:
                print("** no instance found **")
                return
            del objects[key]
            storage.save()
        else:
            print("** class doesn't exist **")
            return

    def help_destroy(self):
        print("""Deletes an instance based on the class name and id
(save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """)

    def do_all(self, line):
        """Prints all string representation of all instances based or not
           to the class name. Ex: $ all BaseModel or $ all.
        Role:
            ** class doesn't exist **: If the class name doesn’t exist,
        """
        args = line.split()
        if len(args) and classes.get(args[0]) is None:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        obj_list = []
        if len(args):
            cls = args[0]
            for k in all_objs:
                if cls == all_objs[k].__class__.__name__:
                    obj_list.append(str(all_objs[k]))
        else:
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
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1 and classes.get(args[0]) is None:
            print("** class doesn't exist **")
            return
        if len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) >= 3 and args[0] in classes:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            cls = classes[args[0]]
            if objects.get(key) is None:
                print("** no instance found **")
                return
            obj = objects[key]
            obj_dict = obj.to_dict()
            obj_dict[args[2]] = args[3]
            obj = cls(**obj_dict)
            objects[key] = obj
            storage.save()
            print(objects)

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
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
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
