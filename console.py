#!/usr/bin/python3

import cmd
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '
    
    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program at end of file (Ctrl-D)
        """
        print()
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything
        """
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the ID"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all 
        instances based or not on the class name"""
        args = arg.split()
        if not args:
            all_instances = list(storage.all().values())
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            all_instances = [value for key, value in storage.all().items() if key.startswith(class_name)]
        print([str(all_instance) for all_instance in all_instances])

    def do_update(self, arg):
        """Updates an instance with a new attribute value"""
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        instance = obj_dict[key]
        # Check if the attribute name is not one of the reserved attributes
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update reserved attribute **")
            return
        # Update the attribute with proper casting
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_count(self, arg):
        """Counts the instances of a class.
        """
        args = arg.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [key for key in storage.all() if key.startswith(args[0] + '.')]
            print(len(matches))

    def do_User(self, arg):
        """Handle actions for the State class"""
        self.default("User", arg)

    def default(self, cls_name, arg):
        """Helper method to handle actions for specific classes"""
        args = arg.split('.')
        command = cls_name + arg
        if len(args) == 2 and args[1] == "all()":
            # class_all = storage.classes()[cls_name]()
            if cls_name in storage.classes():
                self.do_all(cls_name)
                # print(class_all)
        elif len(args) == 2 and args[1] == "count()":
            if cls_name in storage.classes():
                self.do_count(cls_name)
        else:
            super()._handle_class_actions(command)

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
