import sys
import User
import PasswordDatabase

username = sys.argv[0]
password = sys.argv[1]

user = User.User(username, password)
cipher = user.get_cipher()

password_object = PasswordDatabase.PasswordDatabase(cipher, "adam", "passw0Rd", "test password", "this is a thing",
                                                    "hahahahahahahahahahahahaahhahaahha")
pw_json = password_object.generate_object_json()
print(pw_json)
