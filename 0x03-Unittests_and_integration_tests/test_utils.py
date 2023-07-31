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
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
    ) -> None:
        """test for KeyError"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestMemoize(unittest.TestCase):
    """ Memoize test class"""

    def test_memoize(self) -> None:
        """ memoize method with a Test_class"""

        class TestClass:
            def a_method(self) -> None:
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method", return_value=lambda: 42,
        ) as my_call:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            my_call.assert_called_once()
