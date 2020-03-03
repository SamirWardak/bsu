"""
Cryptography by two method python 2.7

First Method Solovay Strassen
first step generate number in range 2**64 and 2**100
second check that number if that is prime number
last step show all generated numbers and result what number is Prime number

Second Method Ferma
first step generate number in range 2**64 and 2**100
second check that number if that is prime number
last step show all generated numbers and result what number is Prime number

Online checker prime number longer 128 symbol: https://ru.numberempire.com/primenumbers.php
"""
import random

solovay_strassen_result, ferma_result = False, False
NSS, NF = 0, 0
NSS_ARRAY, Nf_ARRAY = [], []


def results(number, array, text):
    """
    Print result of tests
    :param number: Prime number
    :type number: int
    :param array: array not prime number
    :type array: list
    :param text: Message text
    :type text: str
    :return: noting
    """
    print(text)
    for i in array:
        print(i)
    print (("Prime number: %s \n \n") % (number))
    return


def solovay_strassen(n, k=10):
    """
    Test for check number in test Solovay Strassen
    :param n: number for testing
    :type n: int
    :param k: iterration for testing
    :type k: int
    :return: result of test
    :rtype: bool
    """
    if n == 2:
        return True
    if not n & 1:
        return False

    def legendre(a, p):
        """
        Check A and B by method Legendre
        :param a: first number for testing
        :type a: int
        :param p: second number for testing
        :type p: int
        :return: number Legendre
        :rtype: int
        """
        if p < 2:
            raise ValueError('p must not be < 2')
        if (a == 0) or (a == 1):
            return a
        if a % 2 == 0:
            r = legendre(a / 2, p)
            if p * p - 1 & 8 != 0:
                r *= -1
        else:
            r = legendre(p % a, a)
            if (a - 1) * (p - 1) & 4 != 0:
                r *= -1
        return r

    for i in range(k):
        a = random.randrange(2, n - 1)
        x = legendre(a, n)
        y = pow(a, (n - 1) / 2, n)
        if (x == 0) or (y != x % n):
            return False

    return True


def FermatPrimalityTest(number):
    """
    Check number by method Fermat
    :param number: number for testing
    :type number: int
    :return: Bool result True or False
    :rtype: bool
    """
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number '''
            randomNumber = random.randint(2, number) - 1
            ''' Test if a^(n-1) = 1 mod n '''
            if (pow(randomNumber, number - 1, number) != 1):
                return False
        return True
    else:
        return False


while solovay_strassen_result is False:
    NSS = random.randrange(2 ** 64, 2 ** 100)
    solovay_strassen_result = solovay_strassen(NSS)
    NSS_ARRAY.append(NSS)

while ferma_result is False:
    NF = random.randrange(2 ** 64, 2 ** 100)
    ferma_result = FermatPrimalityTest(NF)
    Nf_ARRAY.append(NF)

results(NSS, NSS_ARRAY, "Soloveya Shtrassa result:")
results(NF, Nf_ARRAY, "Ferma result:")

