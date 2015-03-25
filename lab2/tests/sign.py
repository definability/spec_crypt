from unittest import TestCase, main

from src.functions import pow_mod

class TestFunctions(TestCase):

  def setUp(self):
    self.p = 0xAF5228967057FE1CB84B92511BE89A47
    self.q = 0x57A9144B382BFF0E5C25C9288DF44D23
    self.a = 0x9E93A4096E5416CED0242228014B67B5
    pass

  def tearDown(self):
    pass

  def test_pow_mod_null(self):
    self.assertEqual(pow_mod(0, 1, 2), 0)
    self.assertEqual(pow_mod(0, 2, self.p), 0)
    self.assertEqual(pow_mod(0, 100, self.q), 0)

  def test_pow_mod_null_pow(self):
    self.assertEqual(pow_mod(1, 0, 2), 1)
    self.assertEqual(pow_mod(self.a, 0, self.p), 1)
    self.assertEqual(pow_mod(self.a, 0, self.q), 1)

  def test_pow_mod_one(self):
    self.assertEqual(pow_mod(1, 1, 2), 1)
    self.assertEqual(pow_mod(1, 2, self.p), 1)
    self.assertEqual(pow_mod(1, 100, self.q), 1)

  def test_pow_mod(self):
    self.assertEqual(pow_mod(self.a, 1, self.p), 0x9E93A4096E5416CED0242228014B67B5)
    self.assertEqual(pow_mod(self.a, 1, self.q), 0x46EA8FBE362817C073FE58FF73571A92)
    self.assertEqual(pow_mod(self.a, 1000, self.p), 0x4E94455148663361949964F7FA9F96F2)
    self.assertEqual(pow_mod(self.a, 1000, self.q), 0x40E7B640381F2DF23ABE1B0AEDA19ED4)

if __name__ == '__main__':
  main()
