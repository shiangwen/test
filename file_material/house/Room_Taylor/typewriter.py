'''
1. 使用在Andrew房間寫下的密碼紙(password.txt)上的內容
2. 在終端機執行骨董的打字機(typewriter.py)就會自動解密，你將得到最重要的線索之一！
3. 記住這個線索，你或許離謎底揭曉不遠了！
'''

# 1 How to open the file in room_Andrew ?
from solve import caesar_cipher

try:
    with open('_file address_', '_mode_') as f:
        pass_code = f.read()
        password = caesar_cipher(pass_code)
        print(password)
except:
    print('!!you don\'t have the password!!')

# 2
# Implement this file, and you may get the correct answer.

# 3
# Record the code or not, it's up to you.