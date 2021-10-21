import unittest
from main import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        l1 = CustomList([5, 1, 3, 7])
        l2 = CustomList([1, 2, 7])
        self.assertEqual([6, 3, 10, 7], l1 + l2)
        l3 = CustomList([3, 4])
        self.assertEqual([4, 6, 3], l3 + [1, 2, 3])
        self.assertEqual([-1, 4, 10], [-2, 2, 3] + l2)

    def test_sub(self):
        l1 = CustomList([5, 1, 3, 7])
        l2 = CustomList([1, 2, 7])
        self.assertEqual([4, -1, -4, 7], l1 - l2)
        l3 = CustomList([3, 4])
        self.assertEqual([2, 2, -3], l3 - [1, 2, 3])
        self.assertEqual([-3, 0, -4], [-2, 2, 3] - l2)

    def test_compare(self):
        l1 = CustomList([5, 1, 3, 7])  # 16
        l2 = CustomList([1, 2, 7])  # 10
        l3 = CustomList([5, 5])  # 10
        self.assertGreater(l1, l2)
        self.assertGreaterEqual(l2, l3)
        self.assertLess(l2, l1)
        self.assertLessEqual(l3, l2)
        self.assertNotEqual(l2, l3)


if __name__ == '__main__':
    unittest.main()