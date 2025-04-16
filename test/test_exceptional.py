import unittest
from mainclass import CumulativeSumAnalysis
from test.TestUtils import TestUtils
import numpy as np
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    
    def test_invalid_data(self):
        """Test handling of invalid data"""
        test_obj = TestUtils()
        try:
            invalid_data = CumulativeSumAnalysis([10, 'invalid', 30])
            invalid_data.cumulative_sum_numpy()
            test_obj.yakshaAssert("TestInvalidData", False, "exceptional")
            print("TestInvalidData = Failed")
        except ValueError as e:
            if str(e) == "could not convert string to float":
                test_obj.yakshaAssert("TestInvalidData", True, "exceptional")
                print("TestInvalidData = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidData", False, "exceptional")
                print("TestInvalidData = Failed")

    def test_empty_data(self):
        """Test handling of empty data"""
        test_obj = TestUtils()
        try:
            empty_data = CumulativeSumAnalysis([])
            empty_data.cumulative_sum_numpy()
            test_obj.yakshaAssert("TestEmptyData", False, "exceptional")
            print("TestEmptyData = Failed")
        except ValueError as e:
            if str(e) == "data is empty":
                test_obj.yakshaAssert("TestEmptyData", True, "exceptional")
                print("TestEmptyData = Passed")
            else:
                test_obj.yakshaAssert("TestEmptyData", False, "exceptional")
                print("TestEmptyData = Failed")
