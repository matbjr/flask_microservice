from providers.cloud_handler import get_config_file


# JSON object for literals and constants
# will be hosted in some cloud storage
# all keys are lower case, Use underscore for longer keys

# need to read from env
cloud_provider = {
    "cloud_host": "dropbox",
    "cloud_config_file": "config.json",
    "cloud_access_key": "vDuiM-56ZzsAAAAAAAAHJGw5MRrhkkeJZ0AJhft11_SCePhuuP2XCVGY3pMGvLBn",
}

# default
config = {
    "application_id": "rm_01",
    "application_version": "0.2.3",
    "application_name": "Reliability Measures microservices",
    "application_org": "Reliability Measures",
    "application_email": "info@reliabilitymeasures.com",
    "application_short_name": "rm_microservices",
    "application_client_id": '807686504198-k9ob5s4g4kunufkrtb6mb9s6sr3dkatu.'
                             'apps.googleusercontent.com',
    "service_url": "http://api.reliabilitymeasures.com/",
    "test_url": "http://localhost:5000/",
    "keywords": {
            "exam": "exam",
            "name": "name",
            "item_responses": "item_responses",
            "student_list": "student_list",
            "item_id": "item_id",
            "response": "response",
            "exclude_items": "exclude_items",
            "id": "id",
            "grad_year": "grad_year",
            "exclude_students": "exclude_students",

            "item_topics": "item_topics",
            "tags": "tags",
            "scored": "scored",
            "topic_branch_hierarchy": "topic_branch_hierarchy",
            "topic_tagged": "topic_tagged",
            "topic_tree": "topic_tree",
            "topic_ids": "topic_ids",
            "topic_hierarchy": "topic_hierarchy",
            "topic_rights": "topic_rights",

            "exclude_threshold_1": 0.09,
            "exclude_threshold_2": 0,
            "exclude_length_1": 0.5,
            "exclude_length_2": 0.8,
            "unknown": "unknown",

            "bad_data": "Invalid data - Not enough students",
            "bad_num_items": "Invalid data - Not enough items",
            "bad_std": "Invalid data - No Std. Dev.",
            "bad_mean": "Invalid data - No mean",
            "no_grad_year": "No graduation years were found, or all students are in the same graduation year",
            "no_assumptions": "No student response assumptions were made",
            "no_topics": "No topics were found",
            "no_students": "No student information was found",
            "no_responses": "No student responses were found",
            "assumed": "assumed",
            "dupes": "duplicates"
    },  
    "services": [
        # use the shot_name key for service path and in response key.
        # Must follow Python/JS variable rules
        {"id": 0},  # left  empty on purpose
        {
            "id": 1,
            "name": "kr20",
            "short_name": "kr20",
            "description": "KR20 value",
            "type": "float"
        },
        {
            "id": 2,
            "name": "Item discrimination",
            "short_name": "idr",
            "description": "Item discrimination, "
                           "Point biserial correlation coefficient",
            "type": "list of floats"
        },
        {
            "id": 3,
            "name": "Item difficulty",
            "short_name": "difficulty",
            "description": "Item difficulty",
            "type": "list of floats"
        },
        {
            "id": 4,
            "name": "scores",
            "short_name": "scores",
            "description": "Test scores",
            "type": "list of floats"
        },
        {
            "id": 5,
            "name": "average",
            "short_name": "average",
            "description": "Student Average",
            "type": "list of floats"
        },
        {
            "id": 6,
            "name": "Test Analysis",
            "short_name": "analysis",
            "api_method": "analyzeTest/",
            "description": "The whole test analysis with all results",
            "type": "list of items"
        },
        {
            "id": 7,
            "name": "Weighted Scores",
            "short_name": "weighted_scores",
            "description": "Weighted test scores",
            "type": "list of floats"
        },
        {
            "id": 8,
            "name": "Weighted Average",
            "short_name": "weighted_avg",
            "description": "Weighted Average of Weighted test scores",
            "type": "float"
        },
        {
            "id": 9,
            "name": "exclude_items",
            "short_name": "exclude",
            "description": "Items to exclude based on idr",
            "type": "list of item ids"
        },
        {
            "id": 10,
            "name": "difficulty_average",
            "short_name": "diff_avg",
            "description": "The average difficulty",
            "type": "float"
        },
        {
            "id": 11,
            "name": "discrimination_average",
            "short_name": "idr_avg",
            "description": "The average item discrimination",
            "type": "float"
        },
        {
            "id": 12,
            "name": "number_of_correct_responses",
            "short_name": "num_correct",
            "description": "The absolute number of an item\'s "
                           "correct responses",
            "type": "list of ints"
        },
        {
            "id": 13,
            "name": "student_response_assumptions",
            "short_name": "assumptions",
            "description": "The assumption of the score 0 for items that "
                           "the student does not have a response for",
            "type": "dictionary of item ids"
        },
        {
            "id": 14,
            "name": "analysis_by_graduation_year",
            "short_name": "grad_year_analysis",
            "description": "Analysis of students\' responses based on "
                           "their graduation year",
            "type": "dictionary of exam analyses"
        },
        {
            "id": 15,
            "name": "topic_right_responses",
            "short_name": "topic_rights",
            "description": "Each students\' number of right responses in each topic",
            "type": "dictionary of topic rights"
        },
        {
            "id": 16,
            "name": "topic_right_averages",
            "short_name": "topic_avgs",
            "description": "The average number of right responses in each topic",
            "type": "dictionary of topic right averages"
        }
    ] 
}

# more to follow


def get_keyword_value(key):
    return config["keywords"][key]


def get_service_config(service_id, field="short_name"):
    return config["services"][service_id][field]


def get_config(config_key):
    return config.get(config_key)


def get_config_from_cloud(cloud_provider):
    try:
        config = get_config_file(cloud_provider)
    except Exception as exc:
        print("Config Exception!")
        