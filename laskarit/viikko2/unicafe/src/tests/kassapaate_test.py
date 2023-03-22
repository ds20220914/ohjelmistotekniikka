import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassapaate=Kassapaate()
	def test_lounaita_myyty_0(self):
		
		self.assertEqual(self.kassapaate.edulliset, 0)
		self.assertEqual(self.kassapaate.maukkaat, 0)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
	
	def test_kateisosto_rahat_riittaa1(self):
		
		maara=self.kassapaate.syo_edullisesti_kateisella(250)
		
		self.assertEqual(self.kassapaate.edulliset, 1)
		self.assertEqual(self.kassapaate.maukkaat, 0)
		self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
		self.assertEqual(maara, 10)
	def test_kateisosto_rahat_riittaa2(self):
		luku=Kassapaate()
                
		maara1=luku.syo_maukkaasti_kateisella(410)
		self.assertEqual(luku.maukkaat, 1)
		self.assertEqual(luku.edulliset, 0)
		self.assertEqual(luku.kassassa_rahaa, 100400)
		self.assertEqual(maara1, 10)
	
	def test_kateisosto_rahat_riittaa3(self):
		luku=Kassapaate()
                
		maara1=luku.syo_maukkaasti_kateisella(400)
		self.assertEqual(luku.maukkaat, 1)
		self.assertEqual(luku.kassassa_rahaa, 100400)
		self.assertEqual(maara1, 0)

	def test_kateisosto_rahat_riittaa4(self):
		luku=Kassapaate()
                
		maara1=luku.syo_edullisesti_kateisella(240)
		self.assertEqual(luku.edulliset, 1)
		self.assertEqual(luku.kassassa_rahaa, 100240)
		self.assertEqual(maara1, 0)

	def test_kateisosto_rahat_eivat_riittaa(self):
		luku=Kassapaate()

		maara1=luku.syo_maukkaasti_kateisella(390)
		self.assertEqual(luku.maukkaat, 0)
		self.assertEqual(luku.kassassa_rahaa, 100000)
		self.assertEqual(maara1, 390)

	def test_kateisosto_rahat_eivat_riittaa1(self):
		luku=Kassapaate()
		maara=luku.syo_edullisesti_kateisella(230)
		
		self.assertEqual(luku.edulliset+luku.maukkaat, 0)
		self.assertEqual(luku.kassassa_rahaa, 100000)
		self.assertEqual(maara, 230)

	def test_korttiosto_rahat_riittaa1(self):
		luku=Kassapaate()
		kortti=Maksukortti(240)
		maara=luku.syo_edullisesti_kortilla(kortti)
		
		self.assertEqual(luku.edulliset, 1)
		self.assertEqual(luku.kassassa_rahaa, 100000)
		self.assertEqual(maara, True)
		
		self.assertEqual(kortti.saldo, 0)
	def test_korttiosto_rahat_riittaa2(self):
		luku=Kassapaate()
		kortti=Maksukortti(400)
		
		maara1=luku.syo_maukkaasti_kortilla(kortti)
		self.assertEqual(luku.maukkaat, 1)
		self.assertEqual(luku.kassassa_rahaa, 100000)
		
		self.assertEqual(maara1, True)
		self.assertEqual(kortti.saldo, 0)
	def test_korttiosto_rahat_riittaa3(self):
		luku=Kassapaate()
		kortti=Maksukortti(410)
                                                          
		maara1=luku.syo_maukkaasti_kortilla(kortti)
		self.assertEqual(luku.maukkaat, 1)
		self.assertEqual(luku.kassassa_rahaa, 100000)
                     
		self.assertEqual(maara1, True)
		self.assertEqual(kortti.saldo, 10)
	def test_korttiosto_rahat_riittaa4(self):
		luku=Kassapaate()
		kortti=Maksukortti(250)
                                                           
		maara1=luku.syo_edullisesti_kortilla(kortti)
		self.assertEqual(luku.edulliset, 1)
		self.assertEqual(luku.kassassa_rahaa, 100000)
                      
		self.assertEqual(maara1, True)
		self.assertEqual(kortti.saldo, 10)
	def test_korttiosto_rahat_eivat_riittaa1(self):
		luku=Kassapaate()
		kortti=Maksukortti(230)
                                                          
		maara1=luku.syo_edullisesti_kortilla(kortti)
		self.assertEqual(luku.edulliset, 0)
		self.assertEqual(luku.kassassa_rahaa, 100000)
                      
		self.assertEqual(maara1, False)
		self.assertEqual(kortti.saldo, 230)
	def test_korttiosto_rahat_eivat_riittaa2(self):
		luku=Kassapaate()
		kortti=Maksukortti(390)
                                                           
		maara1=luku.syo_maukkaasti_kortilla(kortti)
		self.assertEqual(luku.maukkaat, 0)
		self.assertEqual(luku.kassassa_rahaa, 100000)
                      
		self.assertEqual(maara1, False)
		self.assertEqual(kortti.saldo, 390)

	
	def test_lataa_rahaa(self):
		kortti=Maksukortti(0)
		luku=Kassapaate()
		luku.lataa_rahaa_kortille(kortti, 50)
		self.assertEqual(kortti.saldo, 50)
		self.assertEqual(luku.kassassa_rahaa, 100050)
	
	def test_lataa_rahaa1(self):
		kortti=Maksukortti(0)
		luku=Kassapaate()
		luku.lataa_rahaa_kortille(kortti, 0)
		self.assertEqual(kortti.saldo, 0)
		self.assertEqual(luku.kassassa_rahaa, 100000)

	def test_lataa_rahaa2(self):
		kortti=Maksukortti(0)
		luku=Kassapaate()
		maara=luku.lataa_rahaa_kortille(kortti, -1)
		self.assertEqual(kortti.saldo, 0)
		self.assertEqual(luku.kassassa_rahaa, 100000)
		self.assertEqual(maara, None)
