import random

r = random.randint(1,100)
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
		