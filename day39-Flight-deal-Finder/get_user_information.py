# this class to get user information from user input

class GetUserInfor:
    def __init__(self):

        print("""Welcome to Elena's Flight Clue.\n
        We find the best flight deals and email you.
        """)

        self.first_name = input("What is your first name?\n").rstrip()
        self.last_name = input("What is your last name?\n").rstrip()
        self.email = self.check_email().rstrip()

    def check_email(self):
        email_1 = input("What is your email?\n")
        email_2 = input("Type your email again.\n")

        if email_1 == email_2:
            print("You're in the club")
            return email_1

        else:
            print("You may type wrong email, please type again")
            self.check_email()
