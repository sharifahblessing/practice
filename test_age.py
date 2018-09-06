import unittest

from practice.agecal import ageCalculator

class Testclass(unittest.TestCase):

    def test_correct_age_is_calculated(self):
        birth_year = 1990
        assert ageCalculator(birth_year) == 28

    def test_correct_age_is_calculated2(self):
        birth_year = 2020
        assert ageCalculator(birth_year) == None   

    def test_correct_age_is_calculated3(self):
        birth_year = 2018
        assert ageCalculator(birth_year) == 0 