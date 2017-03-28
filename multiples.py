userNum = raw_input("Choose a number >>> ")
userNum = float(userNum)
for multiple in range(2,10):
	answer = userNum * multiple
	print "{} times {} is {}".format(userNum,multiple,answer)