#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
1. 在解開這個謎題之前，解碼器必須先傳入密碼卡(draw_code.txt)的內容，如果你的密碼卡沒有修改過，提示文章會出現問題
2. 最後問題的答案是重要線索的其中之一，請你紀錄下來
'''

# 1 Read the content in the file
with open("draw_code.txt", "r") as f:
    ans_list = f.read().splitlines()

ans_list.sort()

a = ans_list[0]
b = ans_list[1]
c = ans_list[2]
d = ans_list[3]
g = ans_list[4]
h = ans_list[5]
s1 = ans_list[6]
s2 = ans_list[7]

print(' 傳說在冥界最邪惡也最無法侵犯的禁地深處\n', '封印著一排5個顏色各異的天棺，分別是5位域界不同的將領\n', '他們的胸膛各刺上不同的圖騰\n', '他們手持不同的武器\n', '分別有5隻不同的靈獸鎮壓他們')
print()
print(' 將領Morgana埋在紅色天棺.\n',d, '鎮壓將領Katerine.\n', '將領Louis手持',h, '.\n 綠色天棺就在白色天棺的左邊.\n', '沉睡在綠色天棺內的將領手持', a, '.\n 擁有星星圖騰的將領被龍鎮壓.\n', '黃色天棺內的將領擁有樹圖騰.\n', '中間天棺的將領手持劍.\n', '將領Arthur囚禁在第一個天棺.\n', '擁有太陽圖騰的將領沉睡在被熊鎮壓的天棺旁邊.\n', '被', g, '鎮壓的將領沉睡在擁有樹圖騰的將領旁邊.\n', '擁有', c, '圖騰的將領手持盾.\n', '將領Matthrew擁有水圖騰.\n', '將領Arthur沉睡在', b, '旁邊.\n', '擁有', s2, '圖騰的將領沉睡在手持', s1, '的將領旁邊.')
print()
print("誰被狼鎮壓？\n")