import unittest
from meta import CustomPerson


class TestCustomList(unittest.TestCase):
    def setUp(self):
        pass

    def test_meta(self):
        person = CustomPerson('John', 'Smith')
        self.assertEqual(20, person.custom_age)
        self.assertEqual('John', person.custom_first_name)
        self.assertEqual('John Smith', person.custom_full_name())
        self.assertEqual('Smith', person.custom_last_name)
        self.assertEqual(18, person.custom_legal_age())
        self.assertRaises(AttributeError, lambda: person.age)
        self.assertRaises(AttributeError, lambda: person.first_name)
        self.assertRaises(AttributeError, lambda: person.last_name)
        self.assertRaises(AttributeError, lambda: person.full_name())
        self.assertRaises(AttributeError, lambda: person.legal_age())
