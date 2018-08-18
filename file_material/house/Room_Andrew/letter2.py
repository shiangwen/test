'''
1. 這(letter2.jpg)是信上的圖片，試著在終端機執行這個檔案(letter2.py)
2. 嘗試找出數字的規則，兩個問號分別代表什麼數字？
3. 把兩個數字視為一個string(中間不須分隔)，直接寫在密碼板(code_tablet.txt)上
4. 直接在終端機執行解碼器(de_code.py)，應該能給你接下來的關鍵線索，這個線索你可以記下來！
'''
# 1, 2
from PIL import Image

im = Image.open("letter2.jpg")
im.show()

# 3
# with open("__file name__", "_mode_") as f:
#     f.write('code you found')

# 4
# Implement the file(de_code.py)