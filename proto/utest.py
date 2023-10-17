# test_descr_stats.py
import unittest

from test_descr_stats import mean_stat, median_stat

class TestMeanStat(unittest.TestCase):
    def test_mean_int(self):
        self.assertEqual(round(mean_stat([5, 3, 17]), 2), 8.33)

    def test_mean_one_int(self):
        self.assertEqual(median_stat([5]), 5)

    def test_mean_neg_float_int(self):
        self.assertEqual(median_stat([-1, 4, 0.5, 2.5]), 1.5)

class TestMedianStat(unittest.TestCase):
    def test_median_int(self):
        self.assertEqual(median_stat([5, 3, 17]), 5)

    def test_median_neg_int(self):
        self.assertEqual(median_stat([-7]), -7)

    def test_median_many_int(self):
        self.assertEqual(median_stat([2, 1, 11, 8, 5, 2]), 3.5)
    
    def test_median_neg_float_int(self):
        self.assertEqual(median_stat([-1, 4, .5, 2.5]), 1.5)
