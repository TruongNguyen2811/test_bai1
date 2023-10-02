import unittest
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

class TestTinhGiaCuocTaxi(unittest.TestCase):
    # Kiem thu C2
    def test_km_duoi_1(self):
        gia_cuoc = tinh_gia_cuoc_taxi(0.7)
        self.assertEqual(gia_cuoc, 14000)

    def test_km_tu_2_den_12(self):
        gia_cuoc = tinh_gia_cuoc_taxi(7)
        self.assertEqual(gia_cuoc, 113000)

    def test_km_tu_13_den_25(self):
        gia_cuoc = tinh_gia_cuoc_taxi(17)
        self.assertEqual(gia_cuoc, 263000)

    def test_km_tren_25(self):
        gia_cuoc = tinh_gia_cuoc_taxi(50)
        self.assertEqual(gia_cuoc, 691500)
    
    def test_km_0(self):
        gia_cuoc = tinh_gia_cuoc_taxi(0)
        self.assertEqual(gia_cuoc, 0)

if __name__ == '__main__':
    unittest.main()