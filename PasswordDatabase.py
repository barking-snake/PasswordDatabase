import blowfish


class PasswordDatabase:
    def __init__(self, cipher: blowfish.Cipher, username, password, password_type, short_desc, long_desc):
        self.__cipher = cipher
        self.__username = username
        self.__short_desc = short_desc
        self.__long_desc = long_desc
        self.__password = self.encrypt_password(password)
        self.__password_type = password_type

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.decrypt_password(self.__password)

    @password.setter
    def password(self, password):
        self.__password = self.encrypt_password(password)

    @property
    def password_type(self):
        return self.__password_type

    @password_type.setter
    def password_type(self, password_type):
        self.__password_type = password_type

    @property
    def short_desc(self):
        return self.__short_desc

    @short_desc.setter
    def short_desc(self, short_desc):
        self.__short_desc = short_desc

    @property
    def long_desc(self):
        return self.__long_desc

    @long_desc.setter
    def long_desc(self, long_desc):
        self.__long_desc = long_desc

    def decrypt_password(self, password):
        unsalted = self.__cipher.decrypt_block(password).decode("utf-8")
        return unsalted

    def encrypt_password(self, password):
        salted = self.__cipher.encrypt_block(bytes(password, "utf-8"))
        return salted

