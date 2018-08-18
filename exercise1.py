import csv
with open('106_sdata.csv', 'r', encoding='utf-8') as f: #讀取檔案並且成功讀取中文
    reader = csv.reader(f)
    #next(reader)
    #print(reader)
    total_student=0
    for row in reader:
        if row[1]=='國立成功大學':
            total_student+=int(row[6])
    print(total_student)

