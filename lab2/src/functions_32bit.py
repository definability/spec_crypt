SIZE_32BIT = 32
MASK_32BIT = 0xFFFFFFFF

MASK_8BIT = 0xFF
SIZE_8BIT = 8

def reverse_bytes_32bit(n):
  return (((((n & MASK_8BIT) << SIZE_8BIT) |
         (((n >> SIZE_8BIT) & MASK_8BIT))) << (SIZE_8BIT*2)) |
         (((n >> (SIZE_8BIT*2)) & MASK_8BIT) << SIZE_8BIT) |
         ((n >> (SIZE_8BIT*3)) & MASK_8BIT))

def invert_32bit(n):
  return ~n & MASK_32BIT

def rol(x, s):
  s %= SIZE_32BIT
  return ((x << s) | (x >> (SIZE_32BIT-s))) & MASK_32BIT

def ror(x, s):
  s %= SIZE_32BIT
  return ((x >> s) | (x << (SIZE_32BIT-s))) & MASK_32BIT
