data = []
count = 0 
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # % 餘數
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料')

sum_len = 0
avg_len = 0
for d in data:
    sum_len += len(d)
avg_len = sum_len/count
print('平均留言長度是',avg_len)


"""
print(len(data))
print(data[0])
print('-------------')
print(data[1])
"""