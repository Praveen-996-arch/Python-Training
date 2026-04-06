class User:
    #creating a constructor of the object, by initialising attributes using init function
   def __init__(self,user_id,name,username):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.follower = 0

   def upgrading_followers(self):
       self.follower += 1
       user_1.follower += 1

user_1 = User("001", "Isha", "Isha123")
user_1.upgrading_followers()



print(user_1.user_id, user_1.name)
print(user_1.username, user_1.name)
print(user_1.follower)
