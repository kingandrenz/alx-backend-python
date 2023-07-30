#!/usr/bin/env python3
""" task 0 """


import unittest
from parameterized import parameterized
from typing import Tuple, Dict, Union

from utils import (
    access_nested_map,
)


class TestAccessNestedMap(unittest.TestCase):
    """ test the access map function """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_result: Union[Dict, int],
    ) -> None:
        """ test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """test for KeyError"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
