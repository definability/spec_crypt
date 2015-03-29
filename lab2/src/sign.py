from functions_64bit import reverse_bytes_64bit, SIZE_64BIT, MASK_64BIT
from random import randrange
from re import findall

global p, q, a
p = 0xAF5228967057FE1CB84B92511BE89A47
q = 0x57A9144B382BFF0E5C25C9288DF44D23
a = 0x9E93A4096E5416CED0242228014B67B5

def egcd(a, b):
  x,y, u,v = 0,1, 1,0
  while a != 0:
      q, r = b//a, b%a
      m, n = x-u*q, y-v*q
      b,a, x,y, u,v = a,r, u,v, m,n
  gcd = b
  return gcd, x, y

def inv_mod(a, m):
  gcd, x, y = egcd(a, m)
  if gcd != 1:
    return None  # modular inverse does not exist
  else:
    return x % m

def mul_mod(x, y, p):
  return (x*y) % p

def pow_mod_oneliner(a, x, p):
  return reduce(lambda x, y: (x*x*(a if y else 1)) % p, [int(d) for d in bin(x)[2:]], 1)

def pow_mod_simple(a, x, p):
  pow_bin = lambda y, b: (y if b else 1)
  bit_x = [int(digit) for digit in bin(x)[2:]]
  return reduce(lambda x, y: mul_mod(x*x, pow_bin(a, y), p), bit_x, 1)

pow_mod = pow_mod_simple

def calculate_H(h):
  return (reverse_bytes_64bit(h) | (0x00FFFFFFFFFFFF00 << SIZE_64BIT))

def calculate_Z(U, H, a, p):
  return mul_mod(H, pow_mod(a, U, p), p)

def generate_x(Z, q, p):
  while True:
    x = randrange(1, p)
    result = inv_mod(x-Z, q)
    if result is not None:
      break
  return x

def calculate_k(H, U, Z, x, q):
  return mul_mod(U*Z, inv_mod(x-Z, q), q)

def calculate_g(H, U, Z, x, q):
  return mul_mod(x-Z, inv_mod(Z, q), q)

def calculate_S(a, g, p):
  return pow_mod(a, g, p)

def check_kg(h, y, k, S):
  global a
  global p
  return pow_mod(mul_mod(a, S, p), mul_mod(calculate_H(h), pow_mod(S, k, p), p), p) == y % p

def gen_HYKS(h, a, p, q):
  H = calculate_H(h)
  U = randrange(1, p)
  Z = calculate_Z(U, H, a, p)
  x = generate_x(Z, q, p)
  k = calculate_k(H, U, Z, x, q)
  g = calculate_g(H, U, Z, x, q)
  S = calculate_S(a, g, p)
  y = pow_mod(a, x, p)
  return (h, y, k, S)

def parse_signature(signature):
  filename = signature[0]
  H = findall('^H = ([0-9A-Z]+)$', signature[1])[0]
  Y = findall('^Y = ([0-9A-Z]+)$', signature[2])[0]
  K = findall('^K = ([0-9A-Z]+)$', signature[3])[0]
  S = findall('^S = ([0-9A-Z]+)$', signature[4])[0]
  return (filename, int(H, 16), int(Y, 16), int(K, 16), int(S, 16))

def check_signature(signature, h):
  filename, H, y, k, S = parse_signature(signature)
  return check_kg(h, y, k, S)
