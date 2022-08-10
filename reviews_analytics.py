data = []
count = 0

with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(count)

print("檔案讀取完了，總共有", len(data), "筆資料")


reviews_len = 0
for i in range(0, len(data) - 1):
	data_len = len(data[i]) # 每筆留言的長度
	reviews_len = reviews_len + data_len # 加總留言長度

# 平均留言長度
aver_len = reviews_len / len(data)
print("平均留言長度為: ", aver_len, "個字母")

