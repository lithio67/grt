# test_module.py

import unittest
from your_library.module import say, ran, arr

class TestYourLibrary(unittest.TestCase):

    def test_say(self):
        # Redirect stdout to capture print output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        
        say("Hello, World!")
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")
    
    def test_ran(self):
        # Check if the output of ran() is a float and within [0.0, 1.0)
        result = ran()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLess(result, 1.0)

    def test_arr(self):
        # Create an array and verify its type and content
        result = arr('i', [1, 2, 3, 4])
        self.assertIsInstance(result, array)
        self.assertEqual(result.tolist(), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
