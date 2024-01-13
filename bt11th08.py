#!/usr/bin/env python3

chuoi1 = "Tri tue nhan tao ngay nay co the thay the con nguoi trong mot so cong viec nhat dinh"
chuoi2 = "con nguoi ngay nay"

def loc_tu(chuoi1, chuoi2):
	tu_de_loc = set(chuoi2.split())
	ds_tu_da_loc = [word for word in chuoi1.split() if word not in tu_de_loc]
	chuoi_kq = ' '.join(ds_tu_da_loc)
	return chuoi_kq

def luu_file(chuoi, tenfile):
	with open(tenfile, 'w') as file:
		file.write(chuoi)

chuoi_moi = loc_tu(chuoi1, chuoi2)

luu_file(chuoi_moi, "ketqua.txt")
