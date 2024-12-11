def build_profile(first_name, last_name, **kwargs):
    user = {'first_name': first_name, 'last_name': last_name}
    for key, val in kwargs.items():
        user[arg] = val
    return user