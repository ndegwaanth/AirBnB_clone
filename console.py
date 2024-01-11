#!/usr/bin/env python3
"""console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """contain the entry of the command prompt"""
    dictionary = {"BaseModel": BaseModel}
    class_names = ['BaseModel']
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help(self, arg):
        """show the help information"""
        if arg:
            print("EOF {super().help(arg)}")
        else:
            for cmd_tag in dir(self.__class__):
                if cmd_tag.startswith("help"):
                    print(cmd_tag[3:])

    def do_EOF(self, arg):
        """exit on ctrl-D / EOF"""
        return True

    def do_create(self, arg):
        """creating a new instance of the BaseModel save
            it to the json file and print the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.class_names:
            print("** class doesn't exist **")
        else:
            info_class = self.dictionary[arg]
            empty = info_class()
            storage.new(empty)
            storage.save()
            #empty.save()
            print(empty.id)

    def do_show(self, arg):
        """print the string representation of the instance
           based on the class name and id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            info_class = self.dictionary[args[0]]
            id_instance = args[1]
            #key = "{}.{}".format(info_class, id_instance)
            instances = storage.all()
            key = args[0] + "." + id_instance

            if key in instances:
                new_instance = instances[key]
                print(new_instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ delete an instance based on the class name and id
            (save the changes in json file)
        """
        args = arg.split()

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            info_class = self.dictionary[args[0]]
            id_instance = args[1]
            instances = storage.all()
            key = args[0] + "." + id_instance

            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """print all the string representation of all instances based
           or not on the class name
        """
        args = arg.split()
        instances = storage.all()

        if not args:
            result = [str(new_instance) for new_instance in instances.values()]
            print(result)
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            filtered_instance = [str(new_instance) for key, new_instance in instances.items() if key.startswith(class_name + ".")]
            if filtered_instance:
                print(filtered_instance)
            else:
                print("[]")

    def do_update(self, arg):
        """updates an instance basd on the class name and id by
           adding or updating attribute (save the changes in json
           file)
        """
        args = arg.split()

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **i")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        else:
            class_name = args[0]
            id_instance = args[1]
            attribute_name = args[2]
            value = args[3]

            instances = storage.all()
            key = class_name + "." + id_instance

            if key not in instances:
                print("** no instance found **")
            else:
                new_instance = instances[key]

                if hasattr(new_instance, attribute_name):
                    mylist = ['id', 'created_at', 'updated_at']
                    if attribute_name not in mylist:
                        val_type = type(getattr(new_instance, attribute_name))
                        setattr(new_instance, attribute_name, val_type(value))
                        storage.save()
                else:
                    print("** attribute name missing ** ")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
