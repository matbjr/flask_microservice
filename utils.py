def get_list(item, index):
    
    return list(item[index].values())[0]


# JSON object for literals and constants
# will be hosted in some cloud storage
# all keys are lower case, Use underscore for longer keys
config = {
    'cloud_host': 'xxx',
    'cloud_host_credentials':'yyyy',
    'application_id': 'rm_01',
    'application_version': '0.0.1',
    'application_name': 'Reliability Measures microservices',
    'application_short_name': 'rm_microservices',
}

# more to follow
