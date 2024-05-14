#!/usr/bin/python3
"""Module for console.py."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB console."""
    
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **") # Check if class name is missing
            return
        try:
            new_instance = eval(arg)() # Dynamically create instance of specified class
            new_instance.save()  # Save the instance
            print(new_instance.id) # Print the id of the new instance
        except NameError:
            print("** class doesn't exist **")  # Handle non-existent class names

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")  # Check if class name is missing
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")  # Handle non-existent class names
            return
        if len(args) < 2:
            print("** instance id missing **")  # Check if instance id is missing
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")  # Handle non-existent instances
            return
        print(storage.all()[key])  # Print string representation of the instance

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")  # Check if class name is missing
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")  # Handle non-existent class names
            return
        if len(args) < 2:
            print("** instance id missing **")  # Check if instance id is missing
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")  # Handle non-existent instances
            return
        del storage.all()[key]  # Delete the instance from storage
        storage.save()  # Save the changes to the JSON file

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")  # Handle non-existent class names
            return
        print([str(obj) for obj in storage.all().values()])  # Print string representations of all instances

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()  # Split the arguments provided by the user
        if not args:  # Check if no arguments are provided
            print("** class name missing **")
            return
        if args[0] not in storage.classes():  # Check if class name doesn't exist
            print("** class doesn't exist **")
            return
        if len(args) < 2:  # Check if instance id is missing
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]  # Create key to check instance existence
        if key not in storage.all():  # Check if instance doesn't exist
            print("** no instance found **")
            return
        if len(args) < 3:  # Check if attribute name is missing
            print("** attribute name missing **")
            return
        if len(args) < 4:  # Check if value is missing
            print("** value missing **")
            return
        try:
            value = eval(args[3])  # Evaluate the provided value
        except:
            value = args[3]  # If evaluation fails, assign value as string
        setattr(storage.all()[key], args[2], value)  # Set attribute value
        storage.save()

    
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
