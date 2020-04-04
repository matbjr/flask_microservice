from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from analyzeTest import analyze_test


class TestFunctions:

    # testing analyze test
    def test_analyzeTest(self):
        data = {
            "examInfo":
                {"name": "test1"
                 },
            "studentList": [
                {"gradyear": "2022",
                 "id": 1234,
                 "firstname": "John",
                 "lastname": "Smith",
                 "email": "johnsmith@email.com",
                 "itemresponses": [
                     {"itemid": 1, "response": 1},
                     {"itemid": 2, "response": 0},
                     {"itemid": 3, "response": 1},
                     {"itemid": 4, "response": 1},
                     {"itemid": 5, "response": 0},
                     {"itemid": 6, "response": 1}
                 ]
                 },
                {"gradyear": "2022",
                 "id": 1235,
                 "firstname": "Jane",
                 "lastname": "Smath",
                 "email": "janesmath@email.com",
                 "itemresponses": [
                     {"itemid": 1, "response": 0},
                     {"itemid": 2, "response": 1},
                     {"itemid": 3, "response": 1},
                     {"itemid": 4, "response": 1},
                     {"itemid": 5, "response": 1},
                     {"itemid": 6, "response": 1}
                 ]
                 },
                {"gradyear": "2022",
                 "id": 1236,
                 "firstname": "Jake",
                 "lastname": "Jakey",
                 "email": "jakejakey@email.com",
                 "itemresponses": [
                     {"itemid": 1, "response": 0},
                     {"itemid": 2, "response": 1},
                     {"itemid": 3, "response": 0},
                     {"itemid": 4, "response": 0},
                     {"itemid": 5, "response": 0},
                     {"itemid": 6, "response": 1}
                 ]
                 }
            ]
        }

        expected = (
        {'KR20': 0.343}, {'pbcc': [0.049, -0.049, 0.245, 0.245, 0.196, 0.0]},
        {'difficulty': [0.333, 0.667, 0.667, 0.667, 0.333, 1.0]},
        {'scores': [0.667, 0.833, 0.333]}, {'average': 0.611})

        testAnalysis = analyze_test(data)['analysis']

        assert testAnalysis == expected

    # testing the kr_20
    def test_kr20(self):
        sortedData = [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1],
                      [0, 1, 0, 0, 0, 1]]

        expected = 0.343
        kr20 = calculate_kr20(sortedData, 3, 6)['KR20']

        assert kr20 == expected

    # testing the pbcc
    def test_pbcc(self):
        sortedData = [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1],
                      [0, 1, 0, 0, 0, 1]]

        expected = [0.049, -0.049, 0.245, 0.245, 0.196, 0.0]
        pbcc = calculate_pbcc(sortedData, 3, 6)['pbcc']

        assert pbcc == expected

    # testing the difficulty
    def test_difficulty(self):
        sortedData = [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1],
                      [0, 1, 0, 0, 0, 1]]

        expected = [0.333, 0.667, 0.667, 0.667, 0.333, 1.0]
        difficulty = calculate_difficulty(sortedData, 3, 6)['difficulty']

        assert difficulty == expected

    # testing the scores
    def test_scores(self):
        sortedData = [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1],
                      [0, 1, 0, 0, 0, 1]]

        expected = [0.667, 0.833, 0.333]
        scores = calculate_scores(sortedData, 3, 6)['scores']

        assert scores == expected

    # testing the average
    def test_average(self):
        sortedData = [[1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1],
                      [0, 1, 0, 0, 0, 1]]

        expected = 0.611
        average = calculate_average(sortedData, 3, 6)['average']

        assert average == expected
