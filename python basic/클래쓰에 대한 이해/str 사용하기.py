class Profile():
    def __init__(self, profile):
        self.profile = profile
    
    def __str__(self):
        return str(self.profile)
    
profile = Profile({
    "name":"jin",
    "age":32,
})

print(profile)