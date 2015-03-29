from sys import argv, stdin
from src.hash import calculate_hash

if __name__ == '__main__':
  print hex(calculate_hash(stdin))
