def prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def analise_primes(list):
    primes = []
    for number in list:
        if prime(number):
            primes.append(number)
    return primes

def primeiros_100_primos():
    primes = []
    number = 2
    while len(primes) < 100:
        if prime(number):
            primes.append(number)
        number += 1
    return primes

def main():
    primes = primeiros_100_primos()
    print("Os primeiros 100 números primos são:")
    print(primes)
    





if __name__ == "__main__":
    main()