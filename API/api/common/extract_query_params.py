def extract_query_params(query_string):
    query_params = query_string.split('&')
    query_params_dict = dict()
    for param in query_params:
        param_pair = param.split('=')
        query_params_dict[param_pair[0]] = param_pair[1]
    return query_params_dict
