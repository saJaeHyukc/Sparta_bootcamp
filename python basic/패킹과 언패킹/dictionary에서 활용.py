def set_profile(**kwargs):
    profile = {}
    profile["name"] = kwargs.get("name", "-")
    profile["gender"] = kwargs.get("gender", "-")
    profile["birthday"] = kwargs.get("birthday", "-")
    profile["age"] = kwargs.get("age", "-")
    profile["phone"] = kwargs.get("phone", "-")
    profile["email"] = kwargs.get("email", "-")
    
    return profile

user_profile = {
    "name": "lee",
    "gender": "man",
    "age": 32,
    "birthday": "01/01",
    "email": "python@sparta.com",
}

print(set_profile(**user_profile))
""" 아래 코드와 동일
profile = set_profile(
    name="lee",
    gender="man",
    age=32,
    birthday="01/01",
    email="python@sparta.com",
)
"""

# result print
"""
{
    'name': 'lee',
    'gender': 'man',
    'birthday': '01/01',
    'age': 32,
    'phone': '-',
    'email': 'python@sparta.com'
}

"""