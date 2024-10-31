import random

def isPrime(num):
    flag = False

    if num == 0 or num == 1:
        return False
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            return False
        else:
            return True


def randomPrime(start, stop):
    x = 0
    while not isPrime(x):
        x = random.randint(start, stop)
    return x


def generate_key():
  p = randomPrime(100, 1000)
  q = randomPrime(100, 1000)
  while p == q:
      q = randomPrime(100, 1000)
  
  n = p * q
  o_n = (p-1) * (q-1)
  
  e = randomPrime(1, 50)
  
  while (p % e == 0) or (q % e == 0):
      e = randomPrime(1, 50)
  
  d = pow(e, -1, o_n)
  
  return (n, e, d)

