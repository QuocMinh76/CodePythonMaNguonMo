#!/usr/bin/env python3

list = [23, 76, 12, 1, 97, 26, 31]

pos = 0
tong = 0

for i in list:
	if pos % 2 == 0:
		tong = tong + i
	pos = pos + 1

print(f"Tong cac so o vi tri chan trong danh sach {list} la: {tong}")
