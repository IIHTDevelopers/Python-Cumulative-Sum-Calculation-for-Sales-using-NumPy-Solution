import numpy as np
import time

class CumulativeSumAnalysis:
    def __init__(self, sales_data):
        """Initialize NumPy array for sales data and check for invalid or empty data"""
        if not sales_data:
            raise ValueError("data is empty")
        try:
            self.sales_data = np.array(sales_data, dtype=np.float32)
        except ValueError:
            raise ValueError("could not convert string to float")

    def cumulative_sum_numpy(self):
        """Calculate cumulative sum using NumPy"""
        return np.cumsum(self.sales_data)

    def cumulative_sum_python(self):
        """Calculate cumulative sum using Python lists"""
        cumulative_sum = []
        total = 0
        for value in self.sales_data:
            total += value
            cumulative_sum.append(total)
        return cumulative_sum

    def measure_time(self):
        """Measure the time taken for both NumPy and Python operations"""
        start_time = time.time()
        self.cumulative_sum_numpy()
        numpy_time = time.time() - start_time

        start_time = time.time()
        self.cumulative_sum_python()
        python_time = time.time() - start_time

        return numpy_time, python_time
