from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20
from pbcc import calculate_pbcc


class TestFunctions:

    # testing the kr_20
    def test_kr20(self):
        data = {
            "students": [
                {"itemresponses": [1, 0, 1, 1, 0, 1]},
                {"itemresponses": [0, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 1, 0, 0, 0, 1]},
                {"itemresponses": [1, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 0, 0, 0, 1, 0]}
            ]
        }
        expected = 0.726
        kr20 = calculate_kr20(data)['KR20']

        assert kr20 == expected

    # almost same scores
    def test_kr20_low(self):
        data = {
            "students": [
                {"student1": [1, 0, 1, 1, 0, 1]},
                {"student2": [1, 0, 1, 1, 0, 1]},
                {"student3": [1, 0, 1, 1, 0, 1]},
                {"student4": [1, 0, 1, 1, 0, 1]},
                {"student5": [1, 0, 1, 1, 0, 0]}
            ]
        }
        expected = 0
        kr20 = calculate_kr20(data)['KR20']

        assert kr20 == expected

    # missing data
    def test_kr20_invalid(self):
        data = {
            "students": [
                {"student1": [1, 0, 1, 1, 0]},
                {"student2": [0, 1, 1, 1, 1, 1]},
                {"student3": [0, 1, 0, 0, 0, 1]},
                {"student4": [1, 1, 1, 1, 1, 1]},
                {"student5": [0, 0, 0, 0, 1, 0]}
            ]
        }

        kr20_data = calculate_kr20(data)

        assert 'Error' in kr20_data

    # testing the pbcc
    def test_pbcc(self):
        data = {
            "students": [
                {"itemresponses": [1, 0, 1, 1, 0, 1]},
                {"itemresponses": [0, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 1, 0, 0, 0, 1]},
                {"itemresponses": [1, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 0, 0, 0, 1, 0]}
            ]
        }
        expected = [0.353, 0.278, 0.53, 0.53, 0.151, 0.402]
        pbcc = calculate_pbcc(data)['pbcc']

        assert pbcc == expected

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


if __name__ == '__main__':
    tf = TestFunctions()
    tf.test_kr20_low()

    from application import call_service
    import json
    param = json.dumps({"elements": [4,5.6,7,0,22,-4.5]})
    print(call_service(url='http://visonics.net/', method='std/',
                       param=param))


