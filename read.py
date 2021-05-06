data = []
count = 0 
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # % 餘數
        if count % 100000 == 0:
            print('讀取檔案進度第',len(data),'筆')
print('檔案讀取完了,總共有',len(data),'筆資料')
print('----------------------')
#計算平均留言長度
sum_len = 0
avg_len = 0
for d in data:
    sum_len += len(d)
avg_len = sum_len/count
print('平均留言長度是',avg_len)
print('----------------------')

#找出長度小於一百
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有',len(new),'筆留言長度小於一百')
print('第一筆留言資料:',new[0])
print('第二筆留言資料:',new[1])
print('----------------------')


"""
print(len(data))
print(data[0])
print('-------------')
print(data[1])
"""