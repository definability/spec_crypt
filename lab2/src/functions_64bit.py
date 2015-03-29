from functions_32bit import SIZE_8BIT

SIZE_64bit = 64
MASK_64bit = 0xFFFFFFFFFFFFFFFF

def get_64bit_block_size(block):
  if block == 0:
    return 0
  hex_block = "%X"%(block & MASK_64bit)
  return (len(hex_block)/2 + (1 if len(hex_block) % 2 == 1 else 0)) * SIZE_8BIT
