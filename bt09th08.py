#!/usr/bin/env python3
n=0

while n <= 10 or n >= 99:
	n = int(input("Nhap vao mot so n (10 < n < 99): "))
	if n <= 10 or n >= 99:
		print("Vui long nhap lai n!")

count = 0
while count < 10:
	if count == 9:
		print(f"{n}")
	else:
		print(f"{n} ", end='')
	n = n + 3
	count = count + 1
