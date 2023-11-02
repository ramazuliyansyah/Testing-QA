# Modul yang akan diuji
def tambah(a, b):
    return a + b

# Unit test
import unittest

class TestTambah(unittest.TestCase):

    def test_tambah_positif(self):
        self.assertEqual(tambah(2, 3), 5) #Memastikan penjumlahan bilangan positif 2 + 3 = 5 benar

    def test_tambah_negatif(self):
        self.assertEqual(tambah(-2, -3), -5) #Memastikan penjumlahan bilangan negatif -2 + -3 = 5 benar

    def test_tambah_campuran(self):
        self.assertEqual(tambah(-2, 3), 1) #Memastikan penjumlahan bilangan campuran benar -2 + 3 = 1 benar
        self.assertEqual(tambah(2, -3), -1) #Memastikan penjumlahan bilangan campuran benar 2 + -3 = -1 benar

if __name__ == '__main__':
    unittest.main()
