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
    # Kiem thu phan hoach
    def test_km_duoi_1(self):
        gia_cuoc = tinh_gia_cuoc_taxi(0.5)
        self.assertEqual(gia_cuoc, 10000)

    def test_km_tu_2_den_12(self):
        gia_cuoc = tinh_gia_cuoc_taxi(5)
        self.assertEqual(gia_cuoc, 82000)

    def test_km_tu_13_den_25(self):
        gia_cuoc = tinh_gia_cuoc_taxi(15)
        self.assertEqual(gia_cuoc, 234000)

    def test_km_tren_25(self):
        gia_cuoc = tinh_gia_cuoc_taxi(30)
        self.assertEqual(gia_cuoc, 441500)
    # Kiem thu bang quyet dinh
    def test_km_0(self):
        gia_cuoc = tinh_gia_cuoc_taxi(0)
        self.assertEqual(gia_cuoc, 0)

    def test_km_tu_0_1_den_1(self):
        test_cases = [0.1, 0.5, 1]
        for km in test_cases:
            gia_cuoc = tinh_gia_cuoc_taxi(km)
            expected_gia_cuoc = 20000 * km
            self.assertEqual(gia_cuoc, expected_gia_cuoc)

    def test_km_tu_1_1_den_12(self):
        test_cases = [1.1, 5, 12]
        for km in test_cases:
            expected_gia_cuoc = 20000 + (km - 1) * 15500
            gia_cuoc = tinh_gia_cuoc_taxi(km)
            self.assertEqual(gia_cuoc, expected_gia_cuoc)

    def test_km_tu_12_1_den_25(self):
        test_cases = [12.1, 15, 25]
        for km in test_cases:
            expected_gia_cuoc = 20000 + 11 * 15500 + (km - 12) * 14500
            gia_cuoc = tinh_gia_cuoc_taxi(km)
            self.assertEqual(gia_cuoc, expected_gia_cuoc)

    def test_km_lon_hon_25(self):
        test_cases = [25.1, 30, 50]
        for km in test_cases:
            expected_gia_cuoc = 20000 + 11 * 15500 + 13 * 14500 + (km - 25) * 12500
            gia_cuoc = tinh_gia_cuoc_taxi(km)
            self.assertEqual(gia_cuoc, expected_gia_cuoc)

if __name__ == '__main__':
    unittest.main()