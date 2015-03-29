from unittest import TestCase, main
from src.sign import *

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_constants(self):
    self.assertEqual(p, 0xAF5228967057FE1CB84B92511BE89A47)
    self.assertEqual(q, 0x57A9144B382BFF0E5C25C9288DF44D23)
    self.assertEqual(a, 0x9E93A4096E5416CED0242228014B67B5)

  def test_pow_mod_null(self):
    self.assertEqual(pow_mod(0, 1, 2), 0)
    self.assertEqual(pow_mod(0, 2, p), 0)
    self.assertEqual(pow_mod(0, 100, q), 0)

  def test_pow_mod_null_pow(self):
    self.assertEqual(pow_mod(1, 0, 2), 1)
    self.assertEqual(pow_mod(a, 0, p), 1)
    self.assertEqual(pow_mod(a, 0, q), 1)

  def test_pow_mod_one(self):
    self.assertEqual(pow_mod(1, 1, 2), 1)
    self.assertEqual(pow_mod(1, 2, p), 1)
    self.assertEqual(pow_mod(1, 100, q), 1)

  def test_pow_mod(self):
    self.assertEqual(pow_mod(a, 1, p), 0x9E93A4096E5416CED0242228014B67B5)
    self.assertEqual(pow_mod(a, 1, q), 0x46EA8FBE362817C073FE58FF73571A92)
    self.assertEqual(pow_mod(a, 1000, p), 0x4E94455148663361949964F7FA9F96F2)
    self.assertEqual(pow_mod(a, 1000, q), 0x40E7B640381F2DF23ABE1B0AEDA19ED4)

  def test_calculate_H(self):
    self.assertEqual(calculate_H(0x9B7B9A9BCB392075),
                     0xFFFFFFFFFFFF00752039CB9B9A7B9B)

  def test_calculate_Z(self):
    self.assertEqual(calculate_Z(0x45102849236955B39391E710CE7DA065,
                                 0xFFFFFFFFFFFF00752039CB9B9A7B9B, a, p),
                     0x9925513EB71EA5E6D2EBC1FBB811412)

  def test_calculate_g(self):
    self.assertEqual(calculate_g(0xFFFFFFFFFFFF00752039CB9B9A7B9B,
                                 0x45102849236955B39391E710CE7DA065,
                                 0x9925513EB71EA5E6D2EBC1FBB811412,
                                 0xC86AB2E97B5B6526C85DE79A920ED7B5, q),
                     0x18182F08EDC259106C26714AD53DF984)

  def test_calculate_g(self):
    self.assertEqual(calculate_k(0xFFFFFFFFFFFF00752039CB9B9A7B9B,
                                 0x45102849236955B39391E710CE7DA065,
                                 0x9925513EB71EA5E6D2EBC1FBB811412,
                                 0xC86AB2E97B5B6526C85DE79A920ED7B5, q),
                     0x4F5230A13979FE25CFC31A228D0C2FFF)

  def test_calculate_S(self):
    self.assertEqual(calculate_S(a, 0x18182F08EDC259106C26714AD53DF984, p),
                     0x65FE1B8D1A0AA67BF2C7F7043643AB2F)

  def test_check_kg(self):
    self.assertTrue(check_kg(0x9B7B9A9BCB392075,
                             0x3F3529B38308161AB7F0C9973DAE3358,
                             0x4111B9967526351EC1D476D7181670CE,
                             0x56A9FB5EEC59EEFD42E2F403BA987610))

  def test_parse_signature(self):
    signature = ['blank',
        'H = 9B7B9A9BCB392075',
        'Y = 2EB457BAEF6E652B8E260CE487C044DA',
        'K = 4F5230A13979FE25CFC31A228D0C2FFF',
        'S = 65FE1B8D1A0AA67BF2C7F7043643AB2F']
    self.assertEqual(parse_signature(signature),
                     ('blank',
                      0x9B7B9A9BCB392075,
                      0x2EB457BAEF6E652B8E260CE487C044DA,
                      0x4F5230A13979FE25CFC31A228D0C2FFF,
                      0x65FE1B8D1A0AA67BF2C7F7043643AB2F))

  def test_check_signature(self):
    signature = ['blank',
        'H = 9B7B9A9BCB392075',
        'Y = 2EB457BAEF6E652B8E260CE487C044DA',
        'K = 4F5230A13979FE25CFC31A228D0C2FFF',
        'S = 65FE1B8D1A0AA67BF2C7F7043643AB2F']
    self.assertTrue(check_signature(signature, 0x9B7B9A9BCB392075))
    self.assertFalse(check_signature(signature, 0x9B7B9A9BCB392076))

if __name__ == '__main__':
  main()
