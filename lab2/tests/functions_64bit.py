from unittest import TestCase, main

from src.functions_64bit import *

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_constants(self):
    self.assertEqual(SIZE_64BIT, 64)
    self.assertEqual(MASK_64BIT, 0xFFFFFFFFFFFFFFFF)

  def test_get_64bit_block_size(self):
    self.assertEqual(get_64bit_block_size(0), 0)
    self.assertEqual(get_64bit_block_size(1), 8)
    self.assertEqual(get_64bit_block_size(0xF), 8)
    self.assertEqual(get_64bit_block_size(0x10), 8)
    self.assertEqual(get_64bit_block_size(0xF010), 16)
    self.assertEqual(get_64bit_block_size(0x3030300A), 32)

  def test_str_to_64bit_block(self):
    self.assertEqual(str_to_64bit_block(''), 0)
    self.assertEqual(str_to_64bit_block('00'), 0x3030)
    self.assertEqual(str_to_64bit_block('000\n'), 0x3030300A)

if __name__ == '__main__':
  main()
