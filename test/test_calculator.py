import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_calc_pace(self):
        self.assertRaises(AssertionError, calculator.calc_pace, 1, 2.0)
        self.assertRaises(AssertionError, calculator.calc_pace, 1.0, 2)
        self.assertRaises(AssertionError, calculator.calc_pace, 0.0, 2.0)
        self.assertEqual(calculator.calc_pace(1000.0, 240.0), 0.24)
    
    def test_format_pace(self):
        pace = calculator.calc_pace(1000.0, 240.0)
        self.assertRaises(Exception, calculator.format_pace, pace, 'KM')
        self.assertEqual(calculator.format_pace(pace), '4:0.0/km')
        self.assertEqual(calculator.format_pace(pace, 'mile'), '6:26.2/mile')
