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
from num_correct import calculate_num_correct
from assumptions import get_assumptions
from config import get_service_config


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
                        {"item_id": 6, "response": 1},
                        {"item_id": 7, "response": 1}
                    ]
                }
            ],
            'exclude_items':[]
        }

    # testing analyze_test
    def test_analyze(self):
        expected = {'analysis': {'kr20': -1.167,
                                 'idr': {1: 0.0, 2: 0.0, 3: 0.082, 4: 0.082, 5: 0.082, 6: 0.0, 7: -0.082},
                                 'difficulty': {1: 0.667, 2: 0.333, 3: 0.333, 4: 0.333, 5: 0.667, 6: 0.0, 7: 0.667}, 
                                 'scores': [57.1, 71.4, 42.9],
                                 'average': 57.1,
                                 'weighted_scores': [44.4, 55.5, 33.3],
                                 'weighted_avg': 44.4, 
                                 'exclude': [7],
                                 'diff_avg': 0.429, 
                                 'idr_avg': 0.023, 
                                 'num_correct': {1: 1, 2: 2, 3: 2, 4: 2, 5: 1, 6: 3, 7: 1},
                                 'assumptions': {1234: [7], 1235: [7]}}
                    }

        analysis = analyze_test(self.data)
        assert analysis == expected

    # testing the kr_20
    def test_kr20(self):

        expected = -1.167
        kr20 = calculate_kr20(self.data)[get_service_config(1)]

        assert kr20 == expected

    # testing the idr
    def test_idr(self):
        expected = {1: 0.0, 2: 0.0, 3: 0.082, 4: 0.082, 5: 0.082, 6: 0.0, 7: -0.082}
        idr = calculate_idr(self.data)['idr']

        assert idr == expected

    # testing the difficulty
    def test_difficulty(self):

        expected = {1: 0.667, 2: 0.333, 3: 0.333, 4: 0.333, 5: 0.667, 6: 0.0, 7: 0.667}
        difficulty = calculate_difficulty(self.data)['difficulty']
        assert difficulty == expected

    # testing the scores
    def test_scores(self):

        expected = [57.1, 71.4, 42.9]
        scores = calculate_scores(self.data)['scores']
        assert scores == expected

    # testing the average
    def test_average(self):

        expected = 57.1
        average = calculate_average(self.data)['average']

        assert average == expected

    # testing the weighted scores
    def test_weighted_scores(self):

        expected = [44.4, 55.5, 33.3]
        weighted_scores = calculate_weighted_scores(self.data)['weighted_scores']

        assert weighted_scores == expected

    # testing the weighted average
    def test_weighted_avg(self):

        expected = 44.4
        weighted_average = calculate_weighted_average(self.data)['weighted_avg']

        assert weighted_average == expected

    # testing the get excludes
    def test_get_exclude_recos(self):

        expected = [7]
        excludes = get_exclude_recos(self.data)['exclude']

        assert excludes == expected

    # testing the avg difficulty
    def test_difficulty_avg(self):

        expected = 0.429
        diff_avg = calculate_difficulty_average(self.data)['diff_avg']

        assert diff_avg == expected

    # testing the avg idr
    def test_idr_avg(self):

        expected = 0.023
        idr_avg = calculate_idr_average(self.data)['idr_avg']

        assert idr_avg == expected

    # testing the num correct
    def test_num_correct(self):

        expected = {1: 1, 2: 2, 3: 2, 4: 2, 5: 1, 6: 3, 7: 1}
        num_correct = calculate_num_correct(self.data)['num_correct']

        assert num_correct == expected

    
    # testing the assumptions
    def test_assumptions(self):

        expected = {1234: [7], 1235: [7]}
        assumption = get_assumptions(self.data)['assumptions']

        assert assumption == expected
