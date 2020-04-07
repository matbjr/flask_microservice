from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average
from analyze_test import analyze_test_scores
from weighted_scores import calculate_weighted_scores
from weighted_average import calculate_weighted_average
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
        expected = [
            {get_service_config(1): 0.343},
            {get_service_config(2): {1: 0.049, 2: -0.049, 3: 0.245, 4: 0.245, 5: 0.196,
                      6: 0.0}},
            {get_service_config(3): {1: 0.333, 2: 0.667, 3: 0.667, 4: 0.667,
                            5: 0.333, 6: 1.0}},
            {get_service_config(4): [0.667, 0.833, 0.333]},
            {get_service_config(5): 0.611},
            {get_service_config(7): [0.727, 0.909, 0.455]},
            {get_service_config(8): 0.697},
            {get_service_config(9): [2]}
        ]

        analysis = analyze_test_scores(self.data)['analysis']

        assert analysis == expected

    # testing the kr_20
    def test_kr20(self):

        expected = 0.343
        kr20 = calculate_kr20(self.data)[get_service_config(1)]

        assert kr20 == expected

    # testing the pbcc
    def test_pbcc(self):
        expected = {1: 0.049, 2: -0.049, 3: 0.245, 4: 0.245, 5: 0.196, 6: 0.0}
        pbcc = calculate_pbcc(self.data)[get_service_config(2)]

        assert pbcc == expected

    # testing the difficulty
    def test_difficulty(self):

        expected = {1: 0.333, 2: 0.667, 3: 0.667, 4: 0.667, 5: 0.333, 6: 1.0}
        difficulty = calculate_difficulty(self.data)[get_service_config(3)]

        assert difficulty == expected

    # testing the scores
    def test_scores(self):

        expected = [0.667, 0.833, 0.333]
        scores = calculate_scores(self.data)[get_service_config(4)]

        assert scores == expected

    # testing the average
    def test_average(self):

        expected = 0.611
        average = calculate_average(self.data)[get_service_config(5)]

        assert average == expected

    # testing the weighted scores
    def test_weighted_scores(self):

        expected = [0.727, 0.909, 0.455]
        scores = calculate_weighted_scores(self.data)[get_service_config(7)]

        assert scores == expected

    # testing the weighted average
    def test_weighted_avg(self):

        expected = 0.697
        average = calculate_weighted_average(self.data)[get_service_config(8)]

        assert average == expected

    # testing the get excludes
    def test_get_excludes(self):

        expected = [2]
        average = get_excludes(self.data)[get_service_config(9)]

        assert average == expected
