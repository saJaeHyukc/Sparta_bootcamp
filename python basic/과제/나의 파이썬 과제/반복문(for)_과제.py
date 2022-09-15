from pprint import pprint
users = [
    {"name": "Ronald", "age": 30, "math_score": 93, "science_score": 65, "english_score": 93, "social_score": 92},
    {"name": "Amelia", "age": 24, "math_score": 88, "science_score": 52, "english_score": 78, "social_score": 91},
    {"name": "Nathaniel", "age": 28, "math_score": 48, "science_score": 40, "english_score": 49, "social_score": 91},
    {"name": "Sally", "age": 29, "math_score": 100, "science_score": 69, "english_score": 67, "social_score": 82},
    {"name": "Alexander", "age": 30, "math_score": 69, "science_score": 52, "english_score": 98, "social_score": 44},
    {"name": "Madge", "age": 22, "math_score": 52, "science_score": 63, "english_score": 54, "social_score": 47},
    {"name": "Trevor", "age": 23, "math_score": 89, "science_score": 88, "english_score": 69, "social_score": 93},
    {"name": "Andre", "age": 23, "math_score": 50, "science_score": 56, "english_score": 99, "social_score": 54},
    {"name": "Rodney", "age": 16, "math_score": 66, "science_score": 55, "english_score": 58, "social_score": 43},
    {"name": "Raymond", "age": 26, "math_score": 49, "science_score": 55, "english_score": 95, "social_score": 82},
    {"name": "Scott", "age": 15, "math_score": 85, "science_score": 92, "english_score": 56, "social_score": 85},
    {"name": "Jeanette", "age": 28, "math_score": 48, "science_score": 65, "english_score": 77, "social_score": 94},
    {"name": "Sallie", "age": 25, "math_score": 42, "science_score": 72, "english_score": 95, "social_score": 44},
    {"name": "Richard", "age": 21, "math_score": 71, "science_score": 95, "english_score": 61, "social_score": 59},
    {"name": "Callie", "age": 15, "math_score": 98, "science_score": 50, "english_score": 100, "social_score": 74},]
user_list = []
# print(list(users[0].values())[2:6])
def get_filter_user(users):
    for i in range(len(users)):
        a = list(users[i].values())[2:6]
        avg = sum(a) /4
        if avg >= 70:
            u_name = users[i]['name']
            u_age = users[i]['age']
            user_list.append({'name':u_name, 'age':u_age})
    return user_list

filter_users = get_filter_user(users)
pprint(filter_users)
"""
[{'age': 30, 'name': 'Ronald'},
 {'age': 24, 'name': 'Amelia'},
 {'age': 29, 'name': 'Sally'},
 {'age': 23, 'name': 'Trevor'},
 {'age': 26, 'name': 'Raymond'},
 {'age': 15, 'name': 'Scott'},
 {'age': 28, 'name': 'Jeanette'},
 {'age': 21, 'name': 'Richard'},
 {'age': 15, 'name': 'Callie'}]
"""