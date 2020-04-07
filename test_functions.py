from kr20 import calculate_kr20
from idr import calculate_idr
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from analyze_test import analyze_test
from weighted_scores import calculate_weighted_scores
from weighted_average import calculate_weighted_average
from excludes import get_exclude_recos
from difficulty_average import calculate_difficulty_average
from idr_average import calculate_idr_average
from excludes import get_excludes
from utils import get_service_config



class TestFunctions:
    data = None

    # This is called before the actual tests are called.
    # self.data is a class variable that can be used through out the class
    def setup(self):
        self.data = {
            "exam":
            { 
                "name": "test1"
            },
            "student_list": [
                { 
                  "grad_year": "2022",
                  "id": 1234,
                  "first_name": "John",
                  "last_name": "Smith",
                  "email": "johnsmith@email.com",
                  "item_responses": [
                        {"item_id": 1, "response": 1},
                        {"item_id": 2, "response": 0},
                        {"item_id": 3, "response": 1},
                        {"item_id": 4, "response": 1},
                        {"item_id": 5, "response": 0},
                        {"item_id": 6, "response": 1}
                    ]
                },
                { "grad_year": "2022",
                  "id": 1235,
                  "first_name": "Jane",
                  "last_name": "Smath",
                  "email": "janesmath@email.com",
                  "item_responses": [
                        {"item_id": 1, "response": 0},
                        {"item_id": 2, "response": 1},
                        {"item_id": 3, "response": 1},
                        {"item_id": 4, "response": 1},
                        {"item_id": 5, "response": 1},
                        {"item_id": 6, "response": 1}
                    ]
                },
                { "grad_year": "2022",
                  "id": 1236,
                  "first_name": "Jake",
                  "last_name": "Jakey",
                  "email": "jakejakey@email.com",
                  "item_responses": [
                        {"item_id": 1, "response": 0},
                        {"item_id": 2, "response": 1},
                        {"item_id": 3, "response": 0},
                        {"item_id": 4, "response": 0},
                        {"item_id": 5, "response": 0},
                        {"item_id": 6, "response": 1}
                    ]
                }
            ]
        }

    # testing analyze_test
    def test_analyze(self):
        expected = [{'kr20': 0.343},
                    {'idr': {1: 0.049, 2: -0.049, 3: 0.245, 4: 0.245, 5: 0.196, 6: 0.0}},
                    {'difficulty': {1: 0.667, 2: 0.333, 3: 0.333, 4: 0.333, 5: 0.667, 6: 0.0}},
                    {'scores': [66.7, 83.3, 33.3]},
                    {'average': 61.1},
                    {'weighted_s': [57.1, 71.4, 14.3]},
                    {'weighted_avg': 47.6},
                    {'exclude': [1, 2, 6]},
                    {'diff_avg': 0.389},
                    {'idr_avg': 0.114}]

        analysis = analyze_test(self.data)['analysis']
        assert analysis == expected

    # testing the kr_20
    def test_kr20(self):

        expected = 0.343
        kr20 = calculate_kr20(self.data)[get_service_config(1)]

        assert kr20 == expected

    # testing the idr
    def test_idr(self):
        expected = {1: 0.049, 2: -0.049, 3: 0.245, 4: 0.245, 5: 0.196, 6: 0.0}
        idr = calculate_idr(self.data)['idr']

        assert idr == expected

    # testing the difficulty
    def test_difficulty(self):

        expected = {1: 0.667, 2: 0.333, 3: 0.333, 4: 0.333, 5: 0.667, 6: 0.0}
        difficulty = calculate_difficulty(self.data)['difficulty']
        assert difficulty == expected

    # testing the scores
    def test_scores(self):

        expected = [66.7, 83.3, 33.3]
        scores = calculate_scores(self.data)['scores']
        assert scores == expected

    # testing the average
    def test_average(self):

        expected = 61.1
        average = calculate_average(self.data)['average']

        assert average == expected

    # testing the weighted scores
    def test_weighted_scores(self):

        expected = [57.1, 71.4, 14.3]
        weighted_scores = calculate_weighted_scores(self.data)['weighted_s']

        assert weighted_scores == expected

    # testing the weighted average
    def test_weighted_avg(self):

        expected = 47.6
        weighted_average = calculate_weighted_average(self.data)['weighted_avg']

        assert weighted_average == expected

    # testing the get excludes
    def test_get_exclude_recos(self):

        expected = [1, 2, 6]
        excludes = get_exclude_recos(self.data)['exclude']

        assert excludes == expected

    # testing the avg difficulty
    def test_difficulty_avg(self):

        expected = 0.389
        diff_avg = calculate_difficulty_average(self.data)['diff_avg']

        assert diff_avg == expected

    # testing the avg idr
    def test_idr_avg(self):

        expected = 0.114
        idr_avg = calculate_idr_average(self.data)['idr_avg']

        assert idr_avg == expected
