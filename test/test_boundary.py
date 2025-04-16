import unittest
import numpy as np
from mainclass import CumulativeSumAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class BoundaryTests(unittest.TestCase):
    def test_single_element(self):
        """Test system with only one element"""
        single_element = CumulativeSumAnalysis([10])
        result = single_element.cumulative_sum_numpy()
        expected_result = np.array([10], dtype=np.float32)
        test_obj = TestUtils()
        if np.array_equal(result, expected_result):
            test_obj.yakshaAssert("TestSingleElement", True, "boundary")
            print("TestSingleElement = Passed")
        else:
            test_obj.yakshaAssert("TestSingleElement", False, "boundary")
            print("TestSingleElement = Failed")
