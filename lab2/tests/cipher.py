from unittest import TestCase, main

from src.cipher import *

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_padding_zeros_count(self):
    self.assertEqual(get_padding_zeros_count(0), 63)
    self.assertEqual(get_padding_zeros_count(1), 62)
    self.assertEqual(get_padding_zeros_count(63), 0)
    self.assertEqual(get_padding_zeros_count(64), 63)

  def test_padding_bitstring(self):
    self.assertEqual(get_message_padding_bitstring(0), '1' + '0'*63)
    self.assertEqual(get_message_padding_bitstring(1), '1' + '0'*62)
    self.assertEqual(get_message_padding_bitstring(63), '1')
    self.assertEqual(get_message_padding_bitstring(64), '1' + '0'*63)

  def test_cipher_M(self):
    self.assertEqual(cipher_M(0x8000000000000000, 0), 0x1B7B9A9BCB392075)
    self.assertEqual(cipher_M(0x3030300A80000000, 0), 0x754DA839F5174B82)

  def test_G(self):
    self.assertEqual(G(0, 0, True), 0x9B7B9A9BCB392075)
    self.assertEqual(G(0x3030300A, 0, True), 0x457D983375174B82)
    self.assertEqual(G(0x30300A, 0, True), 0x7DBAAD4DF74BA95D)
    self.assertEqual(G(0x3031323334353637, 0, False, 64), 0x51F50DB2B0DCD4BB)
    self.assertEqual(G(0x3839414243440A, 0x51F50DB2B0DCD4BB, True), 0x4C766F149EE1C73D)

if __name__ == '__main__':
  main()
