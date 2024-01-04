#!/usr/bin/env python3

n = int(input("Nhap n: "))

sum = 0

for i in range(0, n + 1):
	sum = sum + i

print("Tong cac so tu 0 den", n, "la", sum, sep=" ")
