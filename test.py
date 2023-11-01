import unittest

# Fungsi sederhana yang akan diuji
def tambah(a, b):
    return a + b

# Membuat sebuah kelas turunan dari unittest.TestCase
class TestTambah(unittest.TestCase):

    # Fungsi untuk menguji apakah fungsi tambah berperilaku sesuai dengan harapan
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 10)  # Memastikan 2 + 3 = 5
        self.assertEqual(tambah(0, 0), 0)  # Memastikan 0 + 0 = 0
        self.assertEqual(tambah(-1, 1), 0)  # Memastikan -1 + 1 = 0
        self.assertEqual(tambah(-1, -1), -2)  # Memastikan -1 + (-1) = -2

if __name__ == '__main__':
    unittest.main()
