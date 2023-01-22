from unittest import TestCase


class TestTest(TestCase):

    def test_creation(self):
        total: int = 5
        self.assertEqual(5, total)
        self.assertEqual(4, total)
