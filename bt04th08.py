#!/usr/bin/env python3

a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
c = int(input("Nhap vao so thu ba: "))

max = a

if b > max:
 	max = b

if c > max:
	max = c

print("So lon nhat trong 3 so da nhap la", max, sep=" ")

