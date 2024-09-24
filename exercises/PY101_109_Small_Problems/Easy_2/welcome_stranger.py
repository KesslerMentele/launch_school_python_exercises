# Welcome Stranger

def greetings(name_list, job_dict):
    full_name = ' '.join(name_list)
    return f'Hello, {full_name}! Nice to have a {job_dict['title']} {job_dict['occupation']} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

