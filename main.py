def tinh_gia_cuoc_taxi(km):
    if 0< km <= 1:
        gia_cuoc = 20000 * km
    elif 1 < km <= 12:
        gia_cuoc = 20000 + (km - 1) * 15500
    elif 12 < km <= 25:
        gia_cuoc = 20000 + 11 * 15500 + (km - 12) * 14500
    elif km<=0:
        gia_cuoc = 0
    else:
        gia_cuoc = 20000 + 11 * 15500 + 13 * 14500 + (km - 25) * 12500
    
    return gia_cuoc

# Nhập số kilômét từ người dùng
km = float(input("Nhập số kilômét: "))

# Tính giá cước và in kết quả
gia_cuoc = tinh_gia_cuoc_taxi(km)
print(f"Khoảng cách: {km} km, Giá cước: {gia_cuoc} VND")