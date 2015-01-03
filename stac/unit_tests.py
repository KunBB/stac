# -*- coding: utf-8 -*-

import unittest
import nonparametric_tests as npt

test_data = {
    "A": [3, 4, 5, 6, 1, 5],
    "B": [4, 3, 2, 1, 2, 6],
    "C": [4, 3, 5, 6, 3, 7],
}

test_data2 = {
    "Tr.1": [5, 1, 16, 5, 10, 19, 10],
    "Tr.2": [4, 3, 12, 4, 9, 18, 7],
    "Tr.3": [7, 1, 22, 3, 7, 28, 6],
    "Tr.4": [10, 0, 22, 5, 13, 37, 8],
    "Tr.5": [12, 2, 35, 4, 10, 58, 7]
}

class TestRankings(unittest.TestCase):        
    def test_friedman(self):
        statistic, p_value, ranking = npt.friedman_test(*test_data.values())
        self.assertListEqual([round(v, 4) for v in ranking], [1.8333, 2.5000, 1.6667])
        self.assertAlmostEqual(statistic, 1.2068965517241395, 4)
        self.assertAlmostEqual(p_value, 0.3392, 4)
    
    def test_aligned_ranks(self):
        statistic, p_value, ranking = npt.friedman_aligned_ranks_test(*test_data.values())
        self.assertListEqual([round(v, 4) for v in ranking], [9.3333, 13.0000, 6.1667])
        self.assertAlmostEqual(statistic, 3.702455111762549, 4)
        self.assertAlmostEqual(p_value, 0.1570, 4)
        
    def test_quade(self):
        statistic, p_value, ranking = npt.quade_test(*test_data.values())
        self.assertListEqual([round(v, 4) for v in ranking], [1.9286, 2.5952, 1.4762])
        self.assertAlmostEqual(statistic, 2.31374172185, 4)
        self.assertAlmostEqual(p_value, 0.1493, 4)

if __name__ == '__main__':
    unittest.main()