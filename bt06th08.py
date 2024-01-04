#!/usr/bin/env python3

list=[]
i=1

def sum_num(list):
	tong = 0
	for i in list:
		tong = tong + i
	return tong

if __name__ == "__main__":
	n = int(input("Ban muon nhap bao nhieu so: "))
	print(f"Nhap {n} so, moi so nam trong khoang tu 100-999")
	while True:
		if i > n:
			break
		print(f"Nhap so thu {i}: ", end="" )
		a = int(input())
		if a >= 100 and a <= 999:
			list.append(a)
			i = i + 1
		else:
			print("So khong nam trong khoang qui dinh (100-999).")
	tong = sum_num(list)

	print("Tong cac so da nhap la", tong)
