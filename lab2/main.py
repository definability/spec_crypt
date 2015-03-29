from sys import argv, stdin
from src.hash import calculate_hash
from src.sign import gen_HYKS, check_signature, a, p, q

if __name__ == '__main__':
  if len(argv) < 2 or len(argv) > 3:
    print "USAGE: %s filename [check_file]"%argv[0]
    exit(1)

  h = 0
  filename = argv[1]
  with open(filename) as input_file:
    h = calculate_hash(input_file)
  if len(argv) == 2:
    H, Y, K, S = gen_HYKS(h, a, p, q)
    print filename
    print 'H = %016X'%H
    print 'Y = %016X'%Y
    print 'K = %016X'%K
    print 'S = %016X'%S
  elif len(argv) == 3:
    with open(argv[2]) as f:
      signature = f.readlines()
      print check_signature(map(str.strip, signature), h)
