import json

from api.utils import get_sorted_responses, get_grad_year_list, get_item_ids, update_input, get_item_topics


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
            "item_topics":[
                {
                    "item_id":"1",
                    "tags":[
                        {
                        "topic_tree":"Biology",
                        "topic_branch_hierarchy":{
                            "0":"Cell biology",
                            "1":"Cells",
                            "2":"Organelles",
                            "3":"Nucleus"
                        },
                        "topic_tagged":"DNA",
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"Biology",
                        "topic_branch_hierarchy":{
                            "0":"Cell biology",
                            "1":"Cells",
                            "2":"Organelles"
                        },
                        "topic_tagged":"Ribosomes",
                        "scored":"Y"
                        }
                    ]
                },
                {
                    "item_id":"2",
                    "tags":[
                        {
                        "topic_tree":"A",
                        "topic_branch_hierarchy":{
                            "0":"B",
                            "1":"C",
                            "2":"D",
                            "3":"E"
                        },
                        "topic_tagged":"f",
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"A",
                        "topic_branch_hierarchy":{
                            "0":"B",
                            "1":"C",
                            "2":"D"
                        },
                        "topic_tagged":"e",
                        "scored":"Y"
                        }
                    ]
                },
                {
                    "item_id":"3",
                    "tags":[
                        {
                        "topic_tree":"G",
                        "topic_branch_hierarchy":{
                            "0":"H",
                            "1":"I",
                            "2":"J",
                            "3":"K"
                        },
                        "topic_tagged":"l",
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"G",
                        "topic_branch_hierarchy":{
                            "0":"H",
                            "1":"I",
                            "2":"J"
                        },
                        "topic_tagged":"k",
                        "scored":"Y"
                        }
                    ]
                },
                {
                    "item_id":"4",
                    "tags":[
                        {
                        "topic_tree":"M",
                        "topic_branch_hierarchy":{
                            "0":"N",
                            "1":"O",
                            "2":"P",
                            "3":"Q"
                        },
                        "topic_tagged":"r",
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"M",
                        "topic_branch_hierarchy":{
                            "0":"N",
                            "1":"O",
                            "2":"P",
                        },
                        "topic_tagged":"q",
                        "scored":"Y"
                        }
                    ]
                },
                {
                    "item_id":"5",
                    "tags":[
                        {
                        "topic_tree":"A",
                        "topic_branch_hierarchy":{
                            "0":"B",
                            "1":"C",
                            "2":"D",
                            "3":"E"
                        },
                        "topic_tagged":"f",
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"m",
                        "topic_branch_hierarchy":{
                            "0":"n",
                            "1":"o",
                            "2":"p",
                        },
                        "topic_tagged":"q",
                        "scored":"Y"
                        }
                    ]
                },
                {
                    "item_id":"6",
                    "tags":[
                        {
                        "topic_tree":"a",
                        "topic_branch_hierarchy":{
                            "0":"b",
                            "1":"c",
                            "2":"d",
                            "3":"e"
                        },
                        "topic_tagged":"f",
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"M",
                        "topic_branch_hierarchy":{
                            "0":"N",
                            "1":"O",
                            "2":"P",
                        },
                        "topic_tagged":"q",
                        "scored":"Y"
                        }
                    ]
                },
            ],
            "student_list": [
                {
                  "grad_year": "2022",
                  "id": "1234",
                  "first_name": "John",
                  "last_name": "Smith",
                  "email": "johnsmith@email.com",
                  "item_responses": [
                        {"item_id": "1", "response": 1},
                        {"item_id": "3", "response": 0},
                        {"item_id": "2", "response": 1},
                        {"item_id": "4", "response": 1},
                        {"item_id": "5", "response": 0},
                        {"item_id": "8", "response": 1}
                    ]
                },
                { "grad_year": "2022",
                  "id": "1235",
                  "first_name": "Jane",
                  "last_name": "Smath",
                  "email": "janesmath@email.com",
                  "item_responses": [
                        {"item_id": "1", "response": 0},
                        {"item_id": "2", "response": 1},
                        {"item_id": "3", "response": 1},
                        {"item_id": "4", "response": 1},
                        {"item_id": "5", "response": 1},
                        {"item_id": "6", "response": 1}
                    ]
                },
                { "grad_year": "2024",
                  "id": "1236",
                  "first_name": "Jake",
                  "last_name": "Jakey",
                  "email": "jakejakey@email.com",
                  "item_responses": [
                        {"item_id": "2", "response": 0},
                        {"item_id": "1", "response": 1},
                        {"item_id": "3", "response": 0},
                        {"item_id": "4", "response": 0},
                        {"item_id": "6", "response": 0},
                        {"item_id": "5", "response": 1},
                        {"item_id": "7", "response": 1}
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

    # testing with item excludes
    def test_with_excludes(self):
        data = {
            "student_list": [
                {
                  "id": 1,
                  "item_responses": [
                        {"item_id": 1, "response": 1},
                        {"item_id": 2, "response": 0},
                        {"item_id": 3, "response": 1},
                        {"item_id": 4, "response": 0}
                    ]
                },
                { 
                  "id": 2,
                  "item_responses": [
                        {"item_id": 1, "response": 0},
                        {"item_id": 2, "response": 1},
                        {"item_id": 3, "response": 0},
                        {"item_id": 4, "response": 1}
                    ]
                },
                { 
                  "id": 3,
                  "item_responses": [
                        {"item_id": 1, "response": 0},
                        {"item_id": 2, "response": 0},
                        {"item_id": 3, "response": 1},
                        {"item_id": 4, "response": 1}
                    ]
                },
                { 
                  "id": 4,
                  "item_responses": [
                        {"item_id": 1, "response": 1},
                        {"item_id": 2, "response": 1},
                        {"item_id": 3, "response": 0},
                        {"item_id": 4, "response": 0}
                    ]
                }
            ],
            "exclude_items": [4]
        }

        expected = [1,2,3]
        id_list = get_item_ids(data)

        assert id_list == expected

    # testing without item excludes
    def test_without_excludes(self):
        data = {
            "student_list": [
                {
                  "id": 1,
                  "item_responses": [
                        {"item_id": 1, "response": 1},
                        {"item_id": 2, "response": 0},
                    ]
                },
                { 
                  "id": 2,
                  "item_responses": [
                        {"item_id": 1, "response": 0},
                        {"item_id": 2, "response": 1},
                    ]
                },
                { 
                  "id": 3,
                  "item_responses": [
                        {"item_id": 1, "response": 0},
                        {"item_id": 2, "response": 1},
                    ]
                }
            ]
        }

        expected = [1, 2]
        id_list = get_item_ids(data)

        assert id_list == expected

    # test update input
    def test_update_input(self):
        data = {
            "student_list": [
                {
                  "item_responses": [
                        {"response": 1},
                        {"response": 0},
                    ]
                }]}

        expected = {
            "student_list": [
                {
                  "id": "1",
                  "item_responses": [
                        {"item_id": "1", "response": 1},
                        {"item_id": "2", "response": 0},
                    ]
                }]}
        updated = update_input(data)

        assert updated == expected

    # test getting item topics
    def test_get_topics(self):
        expected = {"1": [{'Biology': {'Cell biology': {'Cells': {'Organelles': {'Nucleus': {'DNA': None}}}}}},
                        {'Biology': {'Cell biology': {'Cells': {'Organelles': {'Ribosomes': None}}}}}],
                    "2": [{'A': {'B': {'C': {'D': {'E': {'f': None}}}}}},
                        {'A': {'B': {'C': {'D': {'e': None}}}}}],
                    "3": [{'G': {'H': {'I': {'J': {'K': {'l': None}}}}}},
                        {'G': {'H': {'I': {'J': {'k': None}}}}}],
                    "4": [{'M': {'N': {'O': {'P': {'Q': {'r': None}}}}}},
                        {'M': {'N': {'O': {'P': {'q': None}}}}}],
                    "5": [{'A': {'B': {'C': {'D': {'E': {'f': None}}}}}},
                        {'m': {'n': {'o': {'p': {'q': None}}}}}],
                    "6": [{'a': {'b': {'c': {'d': {'e': {'f': None}}}}}},
                        {'M': {'N': {'O': {'P': {'q': None}}}}}]}
        topics = get_item_topics(self.data)
        
        assert topics == expected
