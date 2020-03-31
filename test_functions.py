from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty


class TestFunctions:

    # testing the kr_20
    def test_kr20(self):
        data = {
            "students": [
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":0}},
                {"itemresponses": "0, 1, 1, 1, 1, 1","tableData":{"id":1}},
                {"itemresponses": "0, 1, 0, 0, 0, 1","tableData":{"id":2}},
                {"itemresponses": "1, 1, 1, 1, 1, 1","tableData":{"id":3}},
                {"itemresponses": "0, 0, 0, 0, 1, 0","tableData":{"id":4}}
            ]
        }
        expected = 0.726
        kr20 = calculate_kr20(data)['KR20']

        assert kr20 == expected

    # almost same scores
    def test_kr20_low(self):
        data = {
            "students": [
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":0}},
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":1}},
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":2}},
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":3}},
                {"itemresponses": "1, 0, 1, 1, 0, 0","tableData":{"id":4}}
            ]
        }
        expected = 0
        kr20 = calculate_kr20(data)['KR20']

        assert kr20 == expected

    # missing data
    def test_kr20_invalid(self):
        data = {
            "students": [
                {"itemresponses": "1, 0, 1, 1, 0","tableData":{"id":0}},
                {"itemresponses": "0, 1, 1, 1, 1, 1","tableData":{"id":1}},
                {"itemresponses": "0, 1, 0, 0, 0, 1","tableData":{"id":2}},
                {"itemresponses": "1, 1, 1, 1, 1, 1","tableData":{"id":3}},
                {"itemresponses": "0, 0, 0, 0, 1, 0","tableData":{"id":4}}
            ]
        }

        kr20_data = calculate_kr20(data)

        assert 'item count must be the same' in kr20_data['KR20']

    # testing the pbcc
    def test_pbcc(self):
        data = {
            "students": [
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":0}},
                {"itemresponses": "0, 1, 1, 1, 1, 1","tableData":{"id":1}},
                {"itemresponses": "0, 1, 0, 0, 0, 1","tableData":{"id":2}},
                {"itemresponses": "1, 1, 1, 1, 1, 1","tableData":{"id":3}},
                {"itemresponses": "0, 0, 0, 0, 1, 0","tableData":{"id":4}}
            ]
        }
        expected = [0.353, 0.278, 0.53, 0.53, 0.151, 0.402]
        pbcc = calculate_pbcc(data)['pbcc']

        assert pbcc == expected

<<<<<<< Updated upstream
    # testing the pbcc
    def test_pbcc_invalid(self):
        data = {
            "students": [
                {"itemresponses": [1, 1, 1, 0]},
                {"itemresponses": [0, 1, 0, 1]}
            ]
        }
        expected = [0.353, 0.278, 0.53, 0.53, 0.151, 0.402]
        pbcc_data = calculate_pbcc(data)

        assert 'Invalid' in pbcc_data['pbcc']
=======
    # pbcc missing data
    def test_pbcc_invalid(self):
        data = {
            "students": [
                {"itemresponses": "1, 0, 1, 1, 0","tableData":{"id":0}},
                {"itemresponses": "0, 1, 1, 1, 1, 1","tableData":{"id":1}},
                {"itemresponses": "0, 1, 0, 0, 0, 1","tableData":{"id":2}},
                {"itemresponses": "1, 1, 1, 1, 1, 1","tableData":{"id":3}},
                {"itemresponses": "0, 0, 0, 0, 1, 0","tableData":{"id":4}}
            ]
        }

        pbcc_data = calculate_pbcc(data)

        assert 'Error' in pbcc_data
>>>>>>> Stashed changes

    # testing the difficulty
    def test_difficulty(self):
        data = {
            "students": [
<<<<<<< Updated upstream
                {"itemresponses": [1, 0, 1, 1, 0, 1]},
                {"itemresponses": [0, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 1, 0, 0, 0, 1]},
                {"itemresponses": [1, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 0, 0, 0, 1, 0]}
=======
                {"itemresponses": "1, 0, 1, 1, 0, 1","tableData":{"id":0}},
                {"itemresponses": "0, 1, 1, 1, 1, 1","tableData":{"id":1}},
                {"itemresponses": "0, 1, 0, 0, 0, 1","tableData":{"id":2}},
                {"itemresponses": "1, 1, 1, 1, 1, 1","tableData":{"id":3}},
                {"itemresponses": "0, 0, 0, 0, 1, 0","tableData":{"id":4}}
>>>>>>> Stashed changes
            ]
        }
        expected = [0.4, 0.6, 0.6, 0.6, 0.6, 0.8]
        difficulty = calculate_difficulty(data)['difficulty']

        assert difficulty == expected

    # testing the std
    def test_std(self):
        data = {
            "elements": [4, 5.6, 7, 0, 22, -4.5]
        }
        expected = 8.234
        std = calculate_std(data)['Std']

        assert std == expected

    # testing the summation
    def test_summation(self):
        data = {
            "elements": [4, 5.6, 7, 0, 22, -4.5]
        }
        expected = 34.1
        sm = calculate_summation(data)['Sum']

        assert sm == expected

    # testing the Proportion
    def test_proportion(self):
        data = {
            "twoElements": [4, 5.6, 7, 0, 22, -4.5]
        }
        expected = 0.714
        prop = calculate_proportion(data)['Proportion']

        assert prop == expected



