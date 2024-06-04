import getpass

from bcrypt import hashpw, gensalt

bytes_login = getpass.getpass('Login: ').encode()
bytes_hashed_login = hashpw(bytes_login, gensalt())
str_hashed_login = str(bytes_hashed_login)[2:-1]

bytes_pw = getpass.getpass().encode()
bytes_hashed_pw = hashpw(bytes_pw, gensalt())
str_hashed_pw = str(bytes_hashed_pw)[2:-1]

text = f"""
DEVSYSTEMS_L_DATA={str_hashed_login}
DEVSYSTEMS_S_DATA={str_hashed_login}
"""

with open('.env', 'w', encoding='utf-8') as file:
    file.write(text)

print('Env generated succesfully')
