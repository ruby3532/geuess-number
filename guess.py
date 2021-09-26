import random
start = input('請決定猜數字的範圍開始值： ')
end = input('請決定猜數字的範圍結束值： ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1
	number = input('請猜個數字： ')
	number = int(number)
	if number == r:
		print('終於猜對了')
		print('這是你猜的第', count , '次')
		break
	elif number < r:
		print('比答案小')
	elif number > r:
		print('比答案大')
	print('這是你猜的第', count , '次')
		