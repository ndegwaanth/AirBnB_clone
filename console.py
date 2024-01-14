#!/usr/bin/env python3
"""console"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """contain the entry of the command prompt"""
    dictionary = {"BaseModel": BaseModel, "User": User}
    dictionary["Amenity"] = State
    dictionary["City"] = City
    dictionary["Place"] = Place
    dictionary["Review"] = Review
    dictionary["State"] = State
    class_names = ['BaseModel', 'User']
    class_names.append('Amenity')
    class_names.append('City')
    class_names.append('Place')
    class_names.append('Review')
    class_names.append('state')
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help(self, arg):
        """show the help information"""
        if arg:
            print(f"EOF {super().help(arg)}")
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
            # empty.save()
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
            # key = "{}.{}".format(info_class, id_instance)
            instances = storage.all()
            key = args[0] + "." + id_instance

            # print(f"Key: {key}")
            # print(f"[User]: {instances}")

            if key in instances:
                instance_data = instances[key].to_dict()
                new_instance = info_class(**instance_data)

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

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        args = arg.split('.')

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            dictionary_object = storage.all()
            count = 0
            for key in dictionary_object.keys():
                if key.startswith(args[0] + "."):
                    count += 1
            print(count)

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
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        else:
            class_name = args[0].strip()
            id_instance = args[1].strip()
            attribute_name = args[2].strip()
            value = args[3].strip()

            instances = storage.all()
            # key = "{}.{}".format(class_name, id_instance)
            key = class_name + "." + id_instance
            """debug
            print("Key: ", key)"""

            if key not in instances:
                do_default(key)
                # print("** no instance found **")
            else:
                new_instance = instances[key]
                # debug
                # print("Instances: ", new_instance)

                if hasattr(new_instance, attribute_name):
                    mylist = ['id', 'created_at', 'updated_at']
                    if attribute_name not in mylist:
                        val_type = type(getattr(new_instance, attribute_name))
                        setattr(new_instance, attribute_name, val_type(value))
                        storage.save()
                    else:
                        print("** cannot update id, created_at, or updated_at **")
                else:
                    print("** attribute name missing ** ")

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        valid_commands = ["all", "show", "destroy", "count", "update"]
        match = re.match(r"^(\w+)\s*\((.*)\)$", arg)
        args = arg.split('.')
        my_class = args[0]

        if match:
            command, parameters = match.groups()
            if command in valid_commands:
                if command == "count":
                    return self.do_count(parameters)
                elif command == "show":
                    return self.do_show(parameters)
                elif command == "destroy":
                    return self.do_destroy(parameters)
                elif command == "update":
                    return self.do_update(parameters)
                call = "{} {}".format(command, parameters)
                return getattr(self, "do_" + command)(call)

        match_all = re.match(r"^(\w+)\.all\(\)$", arg)
        match_count = re.match(r"^(\w+)\.count\(\)$", arg)
        match_destroy = re.match(r"^(\w+)\.destroy\((.*?)\)$", arg)
        match_show = re.match(r"^(\w+)\.show\((.*)\)$", arg)
        match_update = re.match(r"^(\w+)\.update\((.*?)\)$", arg)

        if match_all:
            class_name = match_all.group(1)
            return getattr(self, "do_all")(class_name)
        elif match_count:
            class_name = match_count.group(1)
            return getattr(self, "do_count")(class_name)
        elif match_destroy:
            class_name = match_destroy.group(1)
            instance_id = match_destroy.group(2)
            return self.do_destroy("{} {}".format(class_name, instance_id))
        elif match_show:
            class_name, id_instance = match_show.groups(1)
            instance_id = match_show.group(2)
            # parameters = "{} {}".format(class_name, id_instance)
            # return self.do_show(parameters)
            return self.do_show("{} {}".format(class_name, instance_id))
        elif match_update:
            class_name = match_update.group(1)
            update_params = match_update.group(2)
            return self.do_update("{} {}".format(class_name, update_params))
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_all(self, arg):
        """Retrive the number of instances of a given class"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            dictionary_object = storage.all()
            dfile = {}
            if arg:
                for key, value in dictionary_object.items():
                    if key.startswith(arg):
                        dfile[key] = value
                    else:
                        dfile = dictionary_object
                        list = [value.__str__() for value in dfile.values()]
                        if list:
                            print(list)
                        else:
                            print("[]")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
