from unittest import TestCase, main

from src.cipher import *

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testROL(self):
    self.assertEqual(ROL(0, 0), 0)
    self.assertEqual(ROL(0, 1), 0)
    self.assertEqual(ROL(1, 0), 1)
    self.assertEqual(ROL(1, 32), 1)
    self.assertEqual(ROL(1, 64), 1)
    self.assertEqual(ROL(int('1'*4 + '0'*28, 2), 2),
                         int('1'*2 + '0'*28 + '1'*2, 2))
    self.assertEqual(ROL(int('1'*4 + '0'*28, 2), 3),
                         int('1' + '0'*28 + '1'*3, 2))


if __name__ == '__main__':
  main()
