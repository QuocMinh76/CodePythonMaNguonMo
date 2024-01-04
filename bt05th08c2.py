#!/usr/bin/env python3

# Day la chuong trinh cho phep nhap vao bao nhieu so cung duoc, ENTER thi ket thuc
list=[]
i = 1

def find_max(list):
	max = list[0]
	for i in list:
		if i > max:
			max = i
	return max

if __name__ == "__main__":
	print("Nhap cac so (ENTER de ket thuc)")
	while True:
		print(f"So thu {i}: ",  end="")
		a = input()
		i = i + 1
		if not a:
			break
		else:
			a = int(a)
			list.append(a)

	if list:
		max = find_max(list)
		print("So lon nhat trong cac so da nhap la", max)
	else:
		print("Khong co gia tri nao duoc nhap vao")

