import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
       
       self.maksukortti.lataa_rahaa(200)
       self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_kortin_saldo_alussa_oikein(self):
       kortti=Maksukortti(400)
       
       self.assertEqual(str(kortti), "Kortilla on rahaa 4.00 euroa")
    
    def test_medoti_palauttaa_False(self):
       kortti=Maksukortti(350)
       tulos=kortti.ota_rahaa(400)
       self.assertEqual(tulos, False)

    def test_medoti_palauttaa_True(self):
       kortti=Maksukortti(500)
       tulos=kortti.ota_rahaa(400)
       self.assertEqual(tulos, True)
