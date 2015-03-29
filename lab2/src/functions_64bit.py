from functions_32bit import *

SIZE_64BIT = 64
MASK_64BIT = 0xFFFFFFFFFFFFFFFF

def get_64bit_block_size(block):
  if block == 0:
    return 0
  hex_block = "%X"%(block & MASK_64BIT)
  return (len(hex_block)/2 + (1 if len(hex_block) % 2 == 1 else 0)) * SIZE_8BIT

def str_to_64bit_block(chunk):
  result = 0
  for c in chunk:
    result <<= SIZE_8BIT
    result |= ord(c)
  return result

def reverse_bytes_64bit(block):
  return ((reverse_bytes_32bit(block & MASK_32BIT) << SIZE_32BIT) |
           reverse_bytes_32bit((block >> SIZE_32BIT) & MASK_32BIT))
