# TODO: create a class
class User:
    # TODO : initialize starting pieces of date when each time construct happen
    #pass
    # NEW: would be call every time create a new object from this class
    def __init__(self,user_id,username):
        # print("new user being created")
        # TODO: initialize attribute in construct
        self.id = user_id
        self.username = username
        # NEW: set up default value instead of parameter be initialize
        self.follower = 0
        self.following = 0
    def followe(self,user):
        user.follower += 1
        self.following += 1

# TODO: create a object from a class
user_1 = User("001","angela")
user_2 = User("002", "Jack")
user_1.followe(user_2)
print(user_1.follower)
print(user_1.following)

print(user_2.follower)
print(user_2.following)
# TODO: create a attribute
# user_1.id = "001"
# user_1.username = "angela"
# print(user_1.id)
# print(user_1.follower)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jack"
# print(user_2.username)