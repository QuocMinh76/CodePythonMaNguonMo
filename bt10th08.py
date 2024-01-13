#!/usr/bin/env python3

str = input("Nhap moi chuoi: ")

dem_tu = len(str.split())

dem_chuso = sum(c.isalpha() for c in str)
dem_space = sum(c.isspace() for c in str)
dem_dacbiet = len(str) - dem_chuso - dem_space
dem_kytu = dem_chuso + dem_space + dem_dacbiet

print(f"So tu: {dem_tu}")
print(f"So ky tu: {dem_kytu}")
