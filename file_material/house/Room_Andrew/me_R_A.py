#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
這是me的系列檔案
在這裡讀取 3/6 diary(diary_3.6_.txt)的內容，你會更明白步驟順序
'''

## Finish the code below
# 打開筆記本3/5的內容，開始閱讀
f = open("diary_3.6_.txt", "r", encoding='utf-8')
print(f.read())
f.close()