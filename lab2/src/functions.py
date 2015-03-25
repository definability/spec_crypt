def mul_mod(x, y, p):
  return (x*y) % p

def pow_mod_oneliner(a, x, p):
  return reduce(lambda x, y: (x*x*(a if y else 1)) % p, [int(d) for d in bin(x)[2:]], 1)

def pow_mod_simple(a, x, p):
  pow_bin = lambda y, b: (y if b else 1)
  bit_x = [int(digit) for digit in bin(x)[2:]]
  return reduce(lambda x, y: mul_mod(x*x, pow_mod_bin(a, y)), bit_x, 1)

pow_mod = pow_mod_simple

def calculate_k(H, U, Z, x, q):
  return ((U - x*H*Z)/2) % q

def calculate_g(H, U, Z, x, q):
  return ((U + x*H*Z)/2) % q

def check_kg(H, S, a, k, p):
  a_k = pow_mod(a, k, p)
  return mul_mod(a_k, pow_mod(y, H * (mul_mod(S, a_k) % p))) == S % p
