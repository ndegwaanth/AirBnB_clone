#!/usr/bin/env python3
"""this implement the console unittest"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """this class is based on implementing the console.py"""
    def setUp(self):
        """this function is run before the exexution of other function"""
        self.hbnb_command = HBNBCommand()

    def test_destroy_command(self):
        """destroy the keys generated"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='destroy BaseModel 123'):
                self.hbnb_command.onecmd('destroy BaseModel 123')
                self.assertEqual(mock_stdout.getvalue().strip(), '')

    def test_count_command(self):
        """test the number of instances being given"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='count BaseModel'):
                self.hbnb_command.onecmd('count BaseModel')
                self.assertTrue(mock_stdout.getvalue().strip())

    def test_update_command(self):
        """test for the updates"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='update BaseModel 123 name "new_name"'):
                self.hbnb_command.onecmd('update BaseModel 123 name "new_name"')
                self.assertEqual(mock_stdout.getvalue().strip(), '')

    def test_all_command(self):
        """test the display of all the key generated"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='all BaseModel'):
                self.hbnb_command.onecmd('all BaseModel')
                self.assertTrue(mock_stdout.getvalue().strip())
    
    def test_quit_command(self):
        """test the implementation of the command quit"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='quit'):
                self.assertTrue(self.hbnb_command.onecmd('quit'))
                self.assertEqual(mock_stdout.getvalue().strip(), '')

    def test_create_command(self):
        """test the creation of the key"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='create BaseModel'):
                self.hbnb_command.onecmd('create BaseModel')
                self.assertTrue(mock_stdout.getvalue().strip())

    def test_show_command(self):
        """test the display of the dictionary"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='show BaseModel 123'):
                self.hbnb_command.onecmd('show BaseModel 123')
                self.assertTrue(mock_stdout.getvalue().strip())

    def test_default_command(self):
        """test the default command when being implemented in the console"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='invalid_command'):
                self.hbnb_command.onecmd('invalid_command')
                self.assertIn('*** Unknown syntax:', mock_stdout.getvalue().strip())

    def test_help_command(self):
        """test for the help command """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='help'):
                self.hbnb_command.onecmd('help')
                self.assertIn('EOF', mock_stdout.getvalue().strip())

    def test_eof_command(self):
        """test for the end of file"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='EOF'):
                self.assertTrue(self.hbnb_command.onecmd('EOF'))
                self.assertEqual(mock_stdout.getvalue().strip(), '')


if __name__ == '__main__':
    unittest.main()
