class Profile: # 1
    def __init__(self): # 3
        self.profile = { 
            "name":"-",
            "gender":"-",
            "birthday":"-",
            "age":"-",
            "phone":"-",
            "email":"-"
        }
    def set_profile(self, profile): # 5
        self.profile = profile # 6
        
profile1 = Profile() # 2
profile1.set_profile({ # 4
            "name":"진",
            "gender":"남자",
            "birthday":"11월2일",
            "age":"30",
            "phone":"010-1234-5678",
            "email":"jin1234@naver.com"
        })
print(profile1.profile)