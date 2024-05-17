import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()
        self.stdout = StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        """Clean up after the test."""
        sys.stdout = sys.__stdout__

    @patch('sys.stdin', StringIO('quit\n'))
    def test_quit_command(self):
        """Test the quit command."""
        self.console.cmdloop()
        self.assertEqual(self.stdout.getvalue(), '(hbnb)')

    @patch('sys.stdin', StringIO('EOF\n'))
    def test_EOF_command(self):
        """Test the EOF command."""
        self.console.cmdloop()
        self.assertEqual(self.stdout.getvalue(), '(hbnb)')

    def test_create_command(self):
        """Test the create command."""
        self.console.onecmd("create BaseModel")
        self.assertTrue(len(self.stdout.getvalue()) > 0)

    def test_show_command(self):
        """Test the show command."""
        new_instance = BaseModel()
        new_instance.save()
        self.console.onecmd("show BaseModel {}".format(new_instance.id))
        self.assertTrue(len(self.stdout.getvalue()) > 0)

    def test_destroy_command(self):
        """Test the destroy command."""
        new_instance = BaseModel()
        new_instance.save()
        self.console.onecmd("destroy BaseModel {}".format(new_instance.id))
        self.assertFalse(new_instance.id in storage.all())

    def test_all_command(self):
        """Test the all command."""
        self.console.onecmd("all")
        self.assertTrue(len(self.stdout.getvalue()) > 0)

    def test_update_command(self):
        """Test the update command."""
        new_instance = BaseModel()
        new_instance.save()
        self.console.onecmd("update BaseModel {} name Test".format(new_instance.id))
        self.assertEqual(new_instance.name, "Test")

    def test_invalid_command(self):
        """Test invalid command."""
        self.console.onecmd("random_command")
        self.assertTrue(len(self.stdout.getvalue()) > 0)


if __name__ == '__main__':
    unittest.main()
