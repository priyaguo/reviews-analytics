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

print(data[0])


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


#找出 good 留言
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('留言中提到good，一共有',len(good),'筆')
print('第一筆留言:',good[0])
print('----------------------')
 
#快寫法 list comprehension 
good = [d for d in data if 'good' in d]
print(len(good))
print('----------------------')

# #這種比較少用
# bad = ['bad' in d for d in data]
# print(bad)

# # print(len(data))
# # print(data[0])
# # print('-------------')
# # print(data[1])


# 加入字典用法
wc = {}  # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1


for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])
print('----------------------')

while True:
    word = input('請問你想查什麼字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為', wc[word])
    else:
        print(word, '沒有出現過')
print('感謝使用本查詢功能!')
print('----------------------')



