from unittest import TestCase, main

from src.functions_64bit import *

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_get_64bit_block_size(self):
    self.assertEqual(get_64bit_block_size(0), 0)
    self.assertEqual(get_64bit_block_size(1), 8)
    self.assertEqual(get_64bit_block_size(0xF), 8)
    self.assertEqual(get_64bit_block_size(0x10), 8)
    self.assertEqual(get_64bit_block_size(0xF010), 16)
    self.assertEqual(get_64bit_block_size(0x3030300A), 32)

if __name__ == '__main__':
  main()
