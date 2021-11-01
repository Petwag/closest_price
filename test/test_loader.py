from closest_price.loader import Loader
from unittest.mock import patch, mock_open
import unittest
import random


class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_load_input(self):
        self.assertEqual(self.loader.values, [])

        number_of_values = random.randint(0, 30)
        random_list = random.sample(range(10, 100), number_of_values)
        for i in random_list:
            self.loader.load_input(i)

        self.assertEqual(number_of_values, len(self.loader.values))
        self.assertEqual(random_list, self.loader.values)

    @patch(f"{Loader.__module__}.csv")
    def test_load_csv(self, mock_csv):
        mock_csv.reader.return_value = ["1", "2", "3"]

        self.assertEqual(self.loader.values, [])
        with patch(f"{Loader.__module__}.open", mock_open(read_data="foo")):
            self.loader.load_csv("foo_path")

        self.assertEqual(self.loader.values, [int(
            i) for i in mock_csv.reader.return_value])
