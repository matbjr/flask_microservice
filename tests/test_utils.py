import json

from api.utils import get_sorted_responses, get_grad_year_list


class TestUtils:
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
                        {"item_id": 3, "response": 0},
                        {"item_id": 2, "response": 1},
                        {"item_id": 4, "response": 1},
                        {"item_id": 5, "response": 0},
                        {"item_id": 8, "response": 1}
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
                { "grad_year": "2024",
                  "id": 1236,
                  "first_name": "Jake",
                  "last_name": "Jakey",
                  "email": "jakejakey@email.com",
                  "item_responses": [
                        {"item_id": 2, "response": 0},
                        {"item_id": 1, "response": 1},
                        {"item_id": 3, "response": 0},
                        {"item_id": 4, "response": 0},
                        {"item_id": 6, "response": 0},
                        {"item_id": 5, "response": 1},
                        {"item_id": 7, "response": 1}
                    ]
                }
            ],
            "exclude_items":[],
            "exclude_students":[]
        }

    def test_get_sorted_responses(self):

        expected = [[1, 1, 0, 1, 0, 0, 0, 1],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 1, 0, 1, 0]]

        responses = get_sorted_responses(self.data)
        print(responses)

        assert expected == responses

