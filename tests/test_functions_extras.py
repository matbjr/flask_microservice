from api.idr import calculate_idr
from api.analyze_test import analyze_test
from api.analyze_grad_years import analyze_grad_years


class TestFunctions:

    # testing with no grad year
    def test_no_grad_year(self):
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

        expected = "No graduation years were found, or all students are in the same graduation year"
        analysis = analyze_grad_years(data)["grad_year_analysis"]

        assert analysis == expected

    # testing item exclude calcs
    def test_item_excludes_difference(self):
        data_1 = {
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
        data_2 = {
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
            "exclude_items": [1,3]
        }

        idr_1 = calculate_idr(data_1)
        idr_2 = calculate_idr(data_2)

        assert idr_1 != idr_2

    # test analysis with no grad year, student id, or item id
    def test_optional_inputs(self):
        data = {
            "student_list": [
                {
                    "item_responses": [
                        {"response": 1},
                        {"response": 0},
                        {"response": 0}
                    ]
                },
                { 
                    "item_responses": [
                        {"response": 0},
                        {"response": 1},
                        {"response": 1}
                    ]
                },
                { 
                    "item_responses": [
                        {"response": 0},
                        {"response": 1},
                    ]
                }
            ]
        }

        expected = {"analysis": {
                        "assumptions": {"3": {"assumed": ["3"]}},
                        "average": 44.4,
                        "diff_avg": 0.556,
                        "difficulty": {"1": 0.667,
                                    "2": 0.333,
                                    "3": 0.667},
                        "exclude": ["1"],
                        "grad_year_analysis": "No graduation years were found, or all students are in the same graduation year",
                        "idr": {"1": -0.037,
                                "2": 0.037,
                                "3": 0.074},
                        "idr_avg": 0.025,
                        "kr20": -3.0,
                        "num_correct": {"1": 1,
                                        "2": 2,
                                        "3": 1},
                        "scores": {"1": 33.3,
                                "2": 66.7,
                                "3": 33.3},
                        "topic_avgs": "No topics were found",
                        "topic_rights": "No topics were found",
                        "weighted_avg": 40.0,
                        "weighted_scores": {"1": 40.0,
                                            "2": 60.0,
                                            "3": 20.0}},
                    }
        analysis = analyze_test(data)

        assert analysis == expected

    # Test with empty json
    def test_empty_json(self):
        data = {}

        expected = {"analysis": "Invalid data - Not enough students"}
        analysis = analyze_test(data)

        assert analysis == expected

    # Test with one student
    def test_one_student(self):
        data = {"student_list": [{}]}

        expected = {"analysis": "Invalid data - Not enough students"}
        analysis = analyze_test(data)

        assert analysis == expected

    # test with no items
    def test_no_items(self):
        data = {"student_list": [
            {
                "item_responses": []
            },
            {
                "item_responses": []
            },
            {
                "item_responses": []
            }
        ]}

        expected = {"analysis": "Invalid data - Not enough items"}
        analysis = analyze_test(data)

        assert analysis == expected

    # test with one item
    def test_one_item(self):
        data = {"student_list": [
            {
                "item_responses": [{}]
            },
            {
                "item_responses": []
            },
            {
                "item_responses": []
            }
        ]}

        expected = {"analysis": "Invalid data - Not enough items"}
        analysis = analyze_test(data)

        assert analysis == expected

    def test_missing_data_1(self):
        data = {
            "student_list": [
                {
                    "item_responses": [
                        {"response": 1},
                        {"response": 0}
                    ]
                },
                { 
                    "item_responses": [
                        {"response": 0}
                    ]
                },
                { 
                }
            ]
        }

        expected = {"analysis": {"assumptions": {"2": {"assumed": ["2"]},
                                                 "3": {"assumed": ["1", "2"]}},
                                "average": 16.7,
                                "diff_avg": 0.834,
                                "difficulty": {"1": 0.667, "2": 1.0},
                                "exclude": "Invalid data - No mean",
                                "grad_year_analysis": "No graduation years were found, or all "
                                                    "students are in the same graduation year",
                                "idr": "Invalid data - No mean",
                                "idr_avg": "Invalid data - No mean",
                                "kr20": -0.0,
                                "num_correct": {"1": 1, "2": 0},
                                "scores": {"1": 50.0, "2": 0.0, "3": 0.0},
                                "topic_avgs": "No topics were found",
                                "topic_rights": "No topics were found",
                                "weighted_avg": 13.3,
                                "weighted_scores": {"1": 40.0, "2": 0.0, "3": 0.0}}}
        analysis = analyze_test(data)

        assert analysis == expected

    def test_missing_data_2(self):
        data = {
            "item_topics":[
                {
                    "item_id":"1",
                    "tags":[
                        {
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
                        }
                        }
                    ]
                },
                {
                    "item_id":"6",
                    "tags":[
                        {
                        "topic_branch_hierarchy":{
                            "0":"b",
                            "1":"c"
                        },
                        "scored":"Y"
                        },
                        {
                        "topic_tree":"M"
                        }
                    ]
                },
            ],
            "student_list": [
                { 
                  "item_responses": [
                        {"item_id": "1", "response": 1},
                        {"item_id": "2", "response": 0},
                        {"item_id": "3", "response": 1},
                        {"item_id": "4", "response": 1},
                        {"item_id": "5", "response": 0},
                        {"item_id": "6", "response": 1}
                    ]
                },
                { "grad_year": "2022",
                  "email": "janesmath@email.com",
                  "item_responses": [
                        {"item_id": "4", "response": 1},
                        {"item_id": "5", "response": 1},
                        {"item_id": "6", "response": 1}
                    ]
                },
                { "grad_year": "2024",
                  "item_responses": [
                        {"item_id": "1", "response": 0},
                        {"item_id": "2", "response": 1},
                        {"item_id": "3", "response": 0},
                        {"item_id": "4", "response": 0}
                    ]
                }
            ]
        }

        expected = {"analysis": {"assumptions": {"2": {"assumed": ["1",
                                                 "2",
                                                 "3"]},
                               "3": {"assumed": ["5",
                                                 "6"]}},
               "average": 44.5,
               "diff_avg": 0.556,
               "difficulty": {"1": 0.667,
                              "2": 0.667,
                              "3": 0.667,
                              "4": 0.333,
                              "5": 0.667,
                              "6": 0.333},
               "exclude": ["2",
                           "5"],
               "grad_year_analysis": {"2022": "Invalid data - Not enough "
                                              "students",
                                      "2024": "Invalid data - Not enough "
                                              "students",
                                      "unknown": "Invalid data - Not enough "
                                                 "students"},
               "idr": {"1": 0.196,
                       "2": -0.245,
                       "3": 0.196,
                       "4": 0.245,
                       "5": 0.049,
                       "6": 0.245},
               "idr_avg": 0.114,
               "kr20": 0.171,
               "num_correct": {"1": 1,
                               "2": 1,
                               "3": 1,
                               "4": 2,
                               "5": 1,
                               "6": 2},
               "scores": {"1": 66.7,
                          "2": 50.0,
                          "3": 16.7},
               "topic_avgs": [{"topic_hierarchy": ((0,
                                                    "unknown"),
                                                   (1,
                                                    "DNA")),
                               "topic_rights": 0.333},
                              {"topic_hierarchy": ((0,
                                                    "Biology"),
                                                   (1,
                                                    "Cell biology"),
                                                   (2,
                                                    "Cells"),
                                                   (3,
                                                    "Organelles"),
                                                   (4,
                                                    "Ribosomes")),
                               "topic_rights": 0.333},
                              {"topic_hierarchy": ((0,
                                                    "A"),
                                                   (1,
                                                    "B"),
                                                   (2,
                                                    "C"),
                                                   (3,
                                                    "D"),
                                                   (4,
                                                    "E"),
                                                   (5,
                                                    "f")),
                               "topic_rights": 0.0},
                              {"topic_hierarchy": ((0,
                                                    "m"),
                                                   (1,
                                                    "unknown")),
                               "topic_rights": 0.0},
                              {"topic_hierarchy": ((0,
                                                    "unknown"),
                                                   (1,
                                                    "b"),
                                                   (2,
                                                    "c"),
                                                   (3,
                                                    "unknown")),
                               "topic_rights": 0.667},
                              {"topic_hierarchy": ((0,
                                                    "M"),
                                                   (1,
                                                    "unknown")),
                               "topic_rights": 0.667}],
               "topic_rights": {"1": [{"topic_hierarchy": ((0,
                                                            "unknown"),
                                                           (1,
                                                            "DNA")),
                                       "topic_rights": 1},
                                      {"topic_hierarchy": ((0,
                                                            "Biology"),
                                                           (1,
                                                            "Cell biology"),
                                                           (2,
                                                            "Cells"),
                                                           (3,
                                                            "Organelles"),
                                                           (4,
                                                            "Ribosomes")),
                                       "topic_rights": 1},
                                      {"topic_hierarchy": ((0,
                                                            "A"),
                                                           (1,
                                                            "B"),
                                                           (2,
                                                            "C"),
                                                           (3,
                                                            "D"),
                                                           (4,
                                                            "E"),
                                                           (5,
                                                            "f")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "m"),
                                                           (1,
                                                            "unknown")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "unknown"),
                                                           (1,
                                                            "b"),
                                                           (2,
                                                            "c"),
                                                           (3,
                                                            "unknown")),
                                       "topic_rights": 1},
                                      {"topic_hierarchy": ((0,
                                                            "M"),
                                                           (1,
                                                            "unknown")),
                                       "topic_rights": 1}],
                                "2": [{"topic_hierarchy": ((0,
                                                            "unknown"),
                                                           (1,
                                                            "DNA")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "Biology"),
                                                           (1,
                                                            "Cell biology"),
                                                           (2,
                                                            "Cells"),
                                                           (3,
                                                            "Organelles"),
                                                           (4,
                                                            "Ribosomes")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "A"),
                                                           (1,
                                                            "B"),
                                                           (2,
                                                            "C"),
                                                           (3,
                                                            "D"),
                                                           (4,
                                                            "E"),
                                                           (5,
                                                            "f")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "m"),
                                                           (1,
                                                            "unknown")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "unknown"),
                                                           (1,
                                                            "b"),
                                                           (2,
                                                            "c"),
                                                           (3,
                                                            "unknown")),
                                       "topic_rights": 1},
                                      {"topic_hierarchy": ((0,
                                                            "M"),
                                                           (1,
                                                            "unknown")),
                                       "topic_rights": 1}],
                                "3": [{"topic_hierarchy": ((0,
                                                            "unknown"),
                                                           (1,
                                                            "DNA")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "Biology"),
                                                           (1,
                                                            "Cell biology"),
                                                           (2,
                                                            "Cells"),
                                                           (3,
                                                            "Organelles"),
                                                           (4,
                                                            "Ribosomes")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "A"),
                                                           (1,
                                                            "B"),
                                                           (2,
                                                            "C"),
                                                           (3,
                                                            "D"),
                                                           (4,
                                                            "E"),
                                                           (5,
                                                            "f")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "m"),
                                                           (1,
                                                            "unknown")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "unknown"),
                                                           (1,
                                                            "b"),
                                                           (2,
                                                            "c"),
                                                           (3,
                                                            "unknown")),
                                       "topic_rights": 0},
                                      {"topic_hierarchy": ((0,
                                                            "M"),
                                                           (1,
                                                            "unknown")),
                                       "topic_rights": 0}]},
               "weighted_avg": 40.0,
               "weighted_scores": {"1": 60.0,
                                   "2": 40.0,
                                   "3": 20.0}},
           }
        analysis = analyze_test(data)

        assert analysis == expected

