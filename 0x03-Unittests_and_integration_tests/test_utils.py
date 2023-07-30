#!/usr/bin/env python3
"""task 0"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ a class to test access_nested_map function
        from utils modules.
    """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, expected_result):
        """ the test function, takes 3 parameters and
            test if the expected_result == result
        """

        self.assertEqual(access_nested_map(nested_map, path), expected_result)
