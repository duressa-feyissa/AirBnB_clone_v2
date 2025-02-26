#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
HBNBCommand module
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from shlex import split
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """ Command Line Interpreter """

    CLASS = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Exit Command handler function """
        return True
    
    def emptyline(self):
        """ Empty Command handler function """
        pass

    def help_quit(self):
        """ Give information about [quit] command """
        print("Quit command to exit the program")
        print("")
    
    def do_EOF(self, args):
        """ Exit Command handler function """
        return True
    
    def help_EOF(self):
        """ Give information about [EOF] command """
        print("EOF command to exit the program")
        print("")

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
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

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in HBNBCommand.CLASS:
            new_dict = self._key_value_parser(args[1:])
            instance = HBNBCommand.CLASS[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()


    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in HBNBCommand.CLASS:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.CLASS:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in HBNBCommand.CLASS:
            obj_dict = models.storage.all(HBNBCommand.CLASS[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """ Update your command interpreter (console.py) to have these commands: """
        hold = split(arg)
        if len(hold) == 0:
            print("** class name missing **")
        elif len(hold) == 1:
            if hold[0] not in HBNBCommand.CLASS:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(hold) == 2:
            INST = "{}.{}".format(hold[0], hold[1])
            if INST not in models.storage._FileStorage__objects:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(hold) == 3:
            print("** value missing **")
        else:
            INST = "{}.{}".format(hold[0], hold[1])
            OBJ = models.storage._FileStorage__objects[INST]
            if hold[3].isdigit():
                OBJ.__dict__[hold[2]] = int(hold[3])
            elif hold[3].replace('.', '', 1).isdigit():
                OBJ.__dict__[hold[2]] = float(hold[3])
            models.storage.save()

    def default(self, arg):
        """ 
            11 .Update your command interpreter (console.py) to retrieve all
            instances of a class by using: <class name>.all()/
            12 .Update your command interpreter (console.py) to retrieve the number 
            of instances of a class: <class name>.count().
            13. Update your command interpreter (console.py) to retrieve an instance 
            based on its ID: <class name>.show(<id>).
            14. Update your command interpreter (console.py) to destroy an instance 
            based on his ID: <class name>.destroy(<id>).
            15. Update your command interpreter (console.py) to update an instance 
            based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).
            16. Update your command interpreter (console.py) to update an instance based on his 
            ID with a dictionary: <class name>.update(<id>, <dictionary representation>).
        """
        args = arg.split('.', 1)
        if args[0] in HBNBCommand.CLASS:
            if args[1].split('()')[0] == 'all':
                self.do_all(args[0]) 
            elif args[1].split('()')[0] == 'count':
                self.COUNTER(args[0])
            elif args[1].split('(')[0] == 'show':
                self.do_show(args[0] + " " + args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'destroy':
                self.do_destroy(args[0] + " " + args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'update':
                arg0 = args[0]
                if ', ' not in args[1]:
                    arg1 = args[1].split('(')[1].strip(')')
                    self.do_update(arg0 + ' ' + arg1)
                elif ', ' in args[1] and\
                     '{' in args[1] and ':' in args[1]:
                    arg1 = args[1].split('(')[1].strip(')').split(', ', 1)[0]
                    attr_dict = ast.literal_eval(args[1].split('(')[1]
                                                 .strip(')').split(', ', 1)[1])
                    for key, value in attr_dict.items():
                        self.do_update(arg0+' '+arg1+' '+key+' '+str(value))
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) == 2:
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    self.do_update(arg0+' '+arg1+' '+arg2)
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) >= 3:
                    print(args[1])
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    print(arg1)
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    print(arg2)
                    arg3 = args[1].split('(')[1].strip(')').split(', ')[2]
                    print(arg3)
                    self.do_update(arg0+' '+arg1+' '+arg2+' '+arg3)
            else:
                print('*** Unknown syntax: {}'.format(arg))
        else:
            print("** class doesn't exist **")

    @staticmethod
    def COUNTER(name):
        """ to retrieve the number 
            of instances of a class
        """
        count=0
        for key in models.storage._FileStorage__objects.keys():
            if key.split('.')[0] == name:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
