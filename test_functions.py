from std import calculate_std
from summation import calculate_summation
from proportion import calculate_proportion
from kr20 import calculate_kr20
from pbcc import calculate_pbcc
from difficulty import calculate_difficulty
from scores import calculate_scores
from average import calculate_average


class TestFunctions:


    # testing the kr_20
    def test_kr20(self):
        data = { 
            "examInfo": 
                { "name": "test1"
            },
            "studentList": [
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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

        expected = 0.343
        kr20 = calculate_kr20(data)['KR20']

        assert kr20 == expected
        

    # testing the pbcc
    def test_pbcc(self):
        data = { 
            "examInfo": 
                { "name": "test1"
            },
            "studentList": [
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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
        
        expected = {1: 0.049, 2: -0.049, 3: 0.245, 4: 0.245, 5: 0.196, 6: 0.0}
        pbcc = calculate_pbcc(data)['pbcc']

        assert pbcc == expected


    # testing the difficulty
    def test_difficulty(self):
        data = { 
            "examInfo": 
                { "name": "test1"
            },
            "studentList": [
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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

        expected = {1: 0.333, 2: 0.667, 3: 0.667, 4: 0.667, 5: 0.333, 6: 1.0}
        difficulty = calculate_difficulty(data)['difficulty']

        assert difficulty == expected


    # testing the scores
    def test_scores(self):
        data = { 
            "examInfo": 
                { "name": "test1"
            },
            "studentList": [
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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

        expected = [0.667, 0.833, 0.333]
        scores = calculate_scores(data)['scores']

        assert scores == expected


    # testing the average
    def test_average(self):
        data = { 
            "examInfo": 
                { "name": "test1"
            },
            "studentList": [
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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
                { "gradyear": "2022", 
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

        expected = 0.611
        average = calculate_average(data)['average']

        assert average == expected

        data = {
            "students": [
                {"itemresponses": [1, 0, 1, 1, 0, 1]},
                {"itemresponses": [0, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 1, 0, 0, 0, 1]},
                {"itemresponses": [1, 1, 1, 1, 1, 1]},
                {"itemresponses": [0, 0, 0, 0, 1, 0]}
            ]
        }
        expected = 0.6
        average = calculate_average(data)['average']

        assert average == expected

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
