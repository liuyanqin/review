data = []
count = 0
with open('review.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count +=1
		if count % 5 == 0:
			print(len(data))
print('档案读取完了，总共有', len(data), '条')
print(data)
print('---------------------------')
print(data[0])
print(data[2])
print('---------------------------')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均长度为：', sum_len/len(data), '个字')