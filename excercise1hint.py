import csv
with open('106_sdata.csv', 'r', encoding='utf-8') as f: #讀取檔案並且成功讀取中文
    reader = csv.reader(f)

    '''
    分析檔案資料,找出條件與目標加總結果

    for迴圈：
    一次讀一列,
    將第0行編號為5(或第1行字元為國立成功大學)之第6行 進行加總

    '''
    total_student=0
    total_teacher=0
    for row in reader:
        if '''???''':
            total_student+='''???'''
            total_teacher+='''???'''
    print('國立成功大學學生人數為',total_student,'人')
    print('國立成功大學教師人數為',total_teacher,'人')

