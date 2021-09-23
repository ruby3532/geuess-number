import random

r = random.randint(1,100)
number = input('請猜個數字： ')
number = int(number)
while True:
	number = input('請猜個數字： ')
	number = int(number)
	if number == r:
		print('終於猜對了')
		break
	elif number < r:
		print('比答案小')
	elif number > r:
		print('比答案大')
		