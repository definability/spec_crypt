from unittest import TestCase, main

from src.functions_32bit import *

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_constants(self):
    self.assertEqual(SIZE_8BIT, 8)
    self.assertEqual(MASK_8BIT, 0xFF)
    self.assertEqual(SIZE_32BIT, 32)
    self.assertEqual(MASK_32BIT, 0xFFFFFFFF)

  def test_reverse_bytes_32bit(self):
    self.assertEqual(reverse_bytes_32bit(0), 0)
    self.assertEqual(reverse_bytes_32bit(1), 0x01000000)

  def test_invert_32bit(self):
    self.assertEqual(invert_32bit(0), 0xFFFFFFFF)
    self.assertEqual(invert_32bit(0xFFFFFFFF), 0)
    self.assertEqual(invert_32bit(1), 0xFFFFFFFE)
    self.assertEqual(invert_32bit(0xFFFFFFFE), 1)
    self.assertEqual(invert_32bit(0x12345678), 0xEDCBA987)
    self.assertEqual(invert_32bit(0xEDCBA987), 0x12345678)

  def test_rol(self):
    self.assertEqual(rol(0, 0), 0)
    self.assertEqual(rol(0, 1), 0)
    self.assertEqual(rol(1, 0), 1)
    self.assertEqual(rol(1, 32), 1)
    self.assertEqual(rol(1, 64), 1)
    self.assertEqual(rol(int('1'*4 + '0'*28, 2), 2),
                         int('1'*2 + '0'*28 + '1'*2, 2))
    self.assertEqual(rol(int('1'*4 + '0'*28, 2), 3),
                         int('1' + '0'*28 + '1'*3, 2))

  def test_ror(self):
    self.assertEqual(ror(0, 0), 0)
    self.assertEqual(ror(0, 1), 0)
    self.assertEqual(ror(1, 0), 1)
    self.assertEqual(ror(1, 32), 1)
    self.assertEqual(ror(1, 64), 1)
    self.assertEqual(ror(int('1'*2 + '0'*28 + '1'*2, 2), 2),
                         int('1'*4 + '0'*28, 2))
    self.assertEqual(ror(int('1' + '0'*28 + '1'*3, 2), 3),
                         int('1'*4 + '0'*28, 2))


if __name__ == '__main__':
  main()
