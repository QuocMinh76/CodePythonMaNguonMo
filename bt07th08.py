#!/usr/bin/env python3

list=[]
i=1

print("Nhap cac so (ENTER de ket thuc)")
while True:
	print(f"So thu {i}: ",  end="")
	a = input()
	i = i + 1
	if not a:
		break
	else:
		a = int(a)
		if a % 2 == 0:
			list.append(a)

print("Cac so chan trong cac so da nhap la:")
print(list)
