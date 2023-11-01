# Modul yang akan diuji
def tambah(a, b):
    return a + b

# Unit test
import unittest

class TestTambah(unittest.TestCase):

    def test_tambah_positif(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_tambah_negatif(self):
        self.assertEqual(tambah(-2, -3), -5)

    def test_tambah_campuran(self):
        self.assertEqual(tambah(-2, 3), 1)
        self.assertEqual(tambah(2, -3), -1)

 __name__ == '__main__':
    unittest.main()
