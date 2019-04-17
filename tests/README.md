### Acceptance Criteria
#### User.py
1. Init must gracefully handle missing arguments (ValueError)
2. Init must  validate password has the following:
    * At least 8 characters total
    * No more than 24 characters
    * One uppercase character
    * One lowercase character
    * One integer
    * On failure, but gracefully release application and ask user to resubmit
3. Init must ensure username has 8 - 24 characters, a-zA-Z0-9 only
4. Class must return a valid Blowfish cipher
#### PasswordDatabase.py
1. Init should:
    * validate Blowfish cipher
    * password/username At least 8 characters total
    * No more than 24 characters
    * One uppercase character
    * One lowercase character
    * One integer
    * On failure, but gracefully release application and ask user to resubmit
2. Short description is unique
3. Long description field must be truncated to 140 characters and return an INFO log to users if string is truncated
4. Short description should be no more than 16 characters
5. User should be able to encrypt a password with username, password type, and short description (long_desc is optional)
6. User should be able to search for a password by username and return a json object of all passwords that are unlocked
by the given cipher
7. User should be able to search for a password by password_type and return a json object of all passwords unlocked by
the given cipher
8. User should be able to search for a password by short_description and return a json object of the password if
unlocked by given cipher
9. If any search fails due to a cipher being incorrect, the application must gracefully ask the user if they would like
to resubmit their user/cipher object.
10. PasswordDatabase objects should save to DB and ensure that no sensitive data (unsalted password) is stored
11. Salted password must be pulled from database and be unsalted without manual intervention (need?)

