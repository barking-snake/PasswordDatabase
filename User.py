import blowfish
import sqlite3


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__cipher = self.set_database_cipher(password)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def get_cipher(self):
        return self.__cipher

    def db_check_for_user(self):
        try:
            conn = sqlite3.connect('pw.db')
        except Exception as err:
            print(err)

        sql = "SELECT username FROM pw where username = ?"

        req = conn.execute(sql, self.username)
        if req.rowcount > 0:
            exists = True
        else:
            exists = False

        return exists

    def db_insert_user(self):
        try:
            conn = sqlite3.connect('pw.db')
        except Exception as err:
            print(err)

        sql = "INSERT INTO users(username, password) VALUES(?,?)"
        req = conn.cursor()
        req.execute(sql, (self.__username, self.__password))
        return req.lastrowid

    @staticmethod
    def set_database_cipher(password):
        cipher = blowfish.Cipher(bytes(password, "utf-8"))
        return cipher
