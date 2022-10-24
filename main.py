
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

flag = False

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)

for i in range(len(num2)):
	if num1[0] == num2[i]:
		flag = True
		if len(num2) - len(num1) >= i:
			for j in range(len(num1)):
				if num1[j] != num2[i+j]:
					flag = False
		else:
			flag = False
print(flag)


# print ('True') or ('False')
