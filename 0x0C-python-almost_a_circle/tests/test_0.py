#!/usr/bin/python3
"""0-test.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import json


class TestBase(unittest.TestCase):
    """Test class for Base"""

    def test_default_id(self):
        """Test default id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_incrementing_id(self):
        """Test incrementing id"""
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test custom id assignment"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_ids(self):
        """Test mixed id assignment"""
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base()
        self.assertEqual(b5.id, 5)
        b = Base(17)
        self.assertEqual(b.id, 17)

    def test_none_id(self):
        """Test instantiation with None as id"""
        b6 = Base(None)
        self.assertEqual(b6.id, 6)


class TestRectangle(unittest.TestCase):
    """test Rectangle"""

    def test_validate_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 2)

        m = "width must be > 0"
        self.assertEqual(str(e.exception), m)

    def test_validate_str(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("abdi", 2)

        m = "width must be an integer"
        self.assertEqual(str(e.exception), m)

    def test_area(self):
        r7 = Rectangle(3, 3)
        self.assertEqual(r7.area(), 3 * 3)
        self.assertEqual(r7.id, 7)

    def test_display(self):
        expected = " ###\n ###\n"
        exp1 = "\n\n  ##\n  ##\n  ##\n"
        r8 = Rectangle(3, 2, 1, 0)
        r9 = Rectangle(2, 3, 2, 2)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r8.display()
            actual_output = mock_stdout.getvalue()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r9.display()
            actual2 = mock_stdout.getvalue()

        self.assertEqual(actual_output, expected)
        self.assertEqual(actual2, exp1)
        self.assertEqual(r8.id, 8)
        self.assertEqual(r9.id, 9)

    def test_get_witdh(self):
        r10 = Rectangle(4, 8)
        self.assertEqual(r10.width, 4)
        self.assertEqual(r10.id, 10)

    def test_get_x_y(self):
        r11 = Rectangle(4, 8)
        self.assertEqual(r11.x, 0)
        r12 = Rectangle(4, 8, 8, 7)
        self.assertEqual(r12.x, 8)
        r13 = Rectangle(4, 8, 8, 7)
        self.assertEqual(r13.y, 7)
        self.assertEqual(r13.id, 13)

    def test_str(self):
        r14 = Rectangle(4, 5)
        exp = f"[Rectangle] ({r14.id}) 0/0 - 4/5\n"
        with patch('sys.stdout', new_callable=StringIO) as stout:
            print(r14)
            actual = stout.getvalue()
        self.assertEqual(exp, actual)
        self.assertEqual(r14.id, 14)

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 10)
        exp = "[Rectangle] (10) 10/10 - 10/10\n"
        with patch('sys.stdout', new_callable=StringIO) as stout:
            print(r)
            actual = stout.getvalue()
        self.assertEqual(actual, exp)
        with patch('sys.stdout', new_callable=StringIO) as stout:
            r.update(89, 2)
            print(r)
            actual = stout.getvalue()
        exp = "[Rectangle] (89) 10/10 - 2/10\n"
        self.assertEqual(actual, exp)

    def test_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 10)
        exp = "[Rectangle] (10) 1/9 - 10/2\n"
        with patch('sys.stdout', new_callable=StringIO) as stout:
            print(r)
            actual = stout.getvalue()
        self.assertEqual(actual, exp)
        actual = r.to_dictionary()
        exp = {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10}
        self.assertEqual(actual, exp)

    def test_json(self):
        r = Rectangle(10, 7, 2, 8, 300)
        dictionary = r.to_dictionary()
        d = {'x': 2, 'width': 10, 'id': 300, 'height': 7, 'y': 8}
        self.assertEqual(d, dictionary)
        json_dictionary = Base(300).to_json_string([dictionary])
        exp = '[{"x": 2, "width": 10, "id": 300, "height": 7, "y": 8}]'
        j1, j2 = json.loads(exp), json.loads(json_dictionary)
        self.assertEqual(j1, j2)


if __name__ == "__main__":
    unittest.main()
