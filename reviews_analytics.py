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