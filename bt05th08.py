#!/usr/bin/env python3

#Day la chuong trinh quy dinh truoc nhap vao bao nhieu so

list=[]
n=0

def find_max(list):
	max = list[0]
	for i in list:
		if i > max:
			max = i
	return max

if __name__ == "__main__":
	n = int(input("Ban muon nhap bao nhieu so: "))

	for i in range(0, n):
		print(f"Nhap so thu {i + 1}: ", end="" )
		a = int(input())
		list.append(a)

	max = find_max(list)


	print("So lon nhat trong cac so da nhap la", max)
