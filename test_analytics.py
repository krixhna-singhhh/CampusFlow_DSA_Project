import unittest

from campusflow.analytics import ascii_bar_chart


class AnalyticsTests(unittest.TestCase):
    def test_empty_chart(self):
        self.assertEqual(ascii_bar_chart([]), "No data available.")

    def test_chart_contains_label_and_value(self):
        chart = ascii_bar_chart([("DSA", 3)])
        self.assertIn("DSA", chart)
        self.assertIn("3", chart)


if __name__ == "__main__":
    unittest.main()
