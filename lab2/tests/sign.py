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
    self.assertEqual(calculate_Z(0x51F19E4493888D5296F6AD7A45F39509,
                                 0xFFFFFFFFFFFF00752039CB9B9A7B9B, a, p),
                     0x9AAC2FC5E32C300E0B9DAAA5A3F00BE)

  def test_calculate_g(self):
    self.assertEqual(calculate_g(0xFFFFFFFFFFFF00752039CB9B9A7B9B,
                                 0x3F9FB3BA44AF48813E00B2615E42603F,
                                 0x8FAE2EF81BBC94D20C215DE32B80ED2,
                                 0xF25C7373164977E93AAA16F5CCCBB8, q),
                     0x4BE680502A98F0E6BBAA105EFF2E3D51)
    self.assertEqual(calculate_g(0xFFFFFFFFFFFF00752039CB9B9A7B9B,
                                 0x51F19E4493888D5296F6AD7A45F39509,
                                 0x9AAC2FC5E32C300E0B9DAAA5A3F00BE,
                                 0x53B3AC4531DFBE6327A3D02A763EE40C, q),
                     0x40CE09497DE489092C08D535B8189EEB)

  def test_calculate_k(self):
    self.assertEqual(calculate_k(0xFFFFFFFFFFFF00752039CB9B9A7B9B,
                                 0x3F9FB3BA44AF48813E00B2615E42603F,
                                 0x8FAE2EF81BBC94D20C215DE32B80ED2,
                                 0xF25C7373164977E93AAA16F5CCCBB8, q),
                     0x4B6247B5524256A8DE7C6B2AED087011)
    self.assertEqual(calculate_k(0xFFFFFFFFFFFF00752039CB9B9A7B9B,
                                 0x51F19E4493888D5296F6AD7A45F39509,
                                 0x9AAC2FC5E32C300E0B9DAAA5A3F00BE,
                                 0x53B3AC4531DFBE6327A3D02A763EE40C, q),
                     0x112394FB15A404496AEDD8448DDAF61E)

  def test_calculate_S(self):
    self.assertEqual(calculate_S(a, 0x4BE680502A98F0E6BBAA105EFF2E3D51, p),
                     0xACE021CFC8525A4757830F8D5EA01ECC)
    self.assertEqual(calculate_S(a, 0x40CE09497DE489092C08D535B8189EEB, p),
                     0x162C6D8B0F859176220C993B5A947F7E)

  def test_check_kg(self):
    self.assertTrue(check_kg(0x9B7B9A9BCB392075,
                             0x5D1260D9E9AE6B832920A6EA1735D480,
                             0x4B6247B5524256A8DE7C6B2AED087011,
                             0xACE021CFC8525A4757830F8D5EA01ECC))

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
        'Y = 5D1260D9E9AE6B832920A6EA1735D480',
        'K = 4B6247B5524256A8DE7C6B2AED087011',
        'S = ACE021CFC8525A4757830F8D5EA01ECC']
    self.assertTrue(check_signature(signature, 0x9B7B9A9BCB392075))
    self.assertFalse(check_signature(signature, 0x9B7B9A9BCB392076))

if __name__ == '__main__':
  main()
