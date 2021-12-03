from hashlib import md5
from random import choice
import time
import concurrent.futures
import math

PRIMES = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def is_prime(n):
    num = 0
    while num < n:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            num += 1


def main():
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        for prime in executor.map(is_prime, PRIMES):
            pass

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
