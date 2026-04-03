import unittest
from original_code import find_duplicates, slow_fibonacci
from optimized_code import find_duplicates_optimized, fast_fibonacci

class TestOptimizations(unittest.TestCase):
    
    def test_find_duplicates(self):
        test_data = [1, 2, 3, 2, 4, 5, 1, 6, 2]
        expected = [1, 2]
        
        original_result = find_duplicates(test_data)
        optimized_result = find_duplicates_optimized(test_data)
        
        self.assertEqual(set(original_result), set(expected))
        self.assertEqual(set(optimized_result), set(expected))
    
    def test_fibonacci(self):
        n = 10
        expected = 55
        
        original_result = slow_fibonacci(n)
        optimized_result = fast_fibonacci(n)
        
        self.assertEqual(original_result, expected)
        self.assertEqual(optimized_result, expected)
    
    def test_no_regression_edge_cases(self):
        self.assertEqual(find_duplicates_optimized([]), [])
        self.assertEqual(find_duplicates_optimized([1]), [])
        self.assertEqual(find_duplicates_optimized([1, 1]), [1])
        
        self.assertEqual(fast_fibonacci(0), 0)
        self.assertEqual(fast_fibonacci(1), 1)
    
    def test_performance_stability(self):
        import time
        large_list = list(range(1000)) * 2
        
        start = time.time()
        find_duplicates_optimized(large_list)
        opt_time = time.time() - start
        
        self.assertLess(opt_time, 0.5, "Optimized code too slow")

if __name__ == "__main__":
    print("=== RUNNING TESTS ===")
    unittest.main(argv=[''], verbosity=2, exit=False)