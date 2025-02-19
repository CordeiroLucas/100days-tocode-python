class User:
    username:str
    password:str
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
user1 = User("Luxka", "1234")

print(user1.username)