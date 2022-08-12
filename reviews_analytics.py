data = []
count = 0

with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(count)

print("檔案讀取完了，總共有", len(data), "筆資料")


sum_len = 0
for d in data:
    sum_len += len(d) # 加總每筆留言的長度

print("平均留言長度為: ", sum_len / len(data), "個字母")

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("留言長度小於100的資料有", len(new), "筆")

good = []
for d in data:
    if "good" in d:
        good.append(d)
print("留言內容有good的資料一共有", len(good), "筆")
print(good[0])

#文字計數
count_dict = {}
for words in data:
    words_list = words.split()
    for word in words_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
for word in count_dict:
	if count_dict[word] > 1000000:
	    print(word, count_dict[word])
print(len(count_dict))

while True:
    word = input("請輸入你要查詢次數的文字: ")
    if word == "q":
        break
    elif word in count_dict:
    	print(word, "出現過的次數為: ", count_dict[word])
    else:
    	print(word, "沒有出現在文章中")

print("感謝使用本查詢系統")
