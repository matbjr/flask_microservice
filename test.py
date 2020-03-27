from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20


class TestFunctions:

    # testing the kr_20
    def test_kr20(self):
        data = {
            "students": [
                {"itemresponses": [1,0,1,1,0,1]},
                {"itemresponses": [0,1,1,1,1,1]},
                {"itemresponses": [0,1,0,0,0,1]},
                {"itemresponses": [1,1,1,1,1,1]},
                {"itemresponses": [0,0,0,0,1,0]}
            ]
        }
        expected = 0.726
        kr20 = calculate_kr20(data)['KR20']

        assert kr20 == expected

    # testing the std
    def test_std(self):
        data = {
            "elements": [4, 5.6,7, 0, 22,-4.5]
        }
        expected = 8.234
        std = calculate_std(data)['Std']

        assert std == expected

    # testing the summation
    def test_summation(self):
        data = {
            "elements": [4, 5.6,7, 0, 22,-4.5]
        }
        expected = 34.1
        sm = calculate_summation(data)['Sum']

        assert sm == expected

    # testing the Proportion
    def test_proportion(self):
        data = {
            "twoElements": [4, 5.6,7, 0, 22,-4.5]
        }
        expected = 0.714
        prop = calculate_proportion(data)['Proportion']

        assert prop == expected