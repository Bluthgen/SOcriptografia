# -*- coding: utf-8 -*-
from math import sqrt; from itertools import count, islice
import random
from math import gcd as bltin_gcd
import sys
import binascii

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

p= 187072209578355573530071658587684226515959365500337
p1 = 18014398509481417
q= 187072209578355573530071658587684226515959365500199
q1 = 18014398509481217

n = 34996011596528190789960035633881941845650710894044463666168900345499553397854271592575144469908067063
t= 34996011596528190789960035633881941845650710894044089521749743634352493254537096224122112551177066528

e= 58341599
d= 20186318348726963390232812105955486341310902298677969473062257141148354731647635787647811512273763551


def encode(texto):
    temp= texto.encode('utf-8')
    temp2= binascii.hexlify(temp)
    return int(temp2, 16)

def decode(codigo):
    aux= hex(codigo)
    aux2= aux[2:]
    temp= aux2.encode('ascii')
    temp2= binascii.unhexlify(temp)
    return temp2.decode('utf-8')

def encrypt(num, e, n):
    return pow(num, e, n)

def decrypt(num, d, n):
    return pow(num, d, n)

def testaEncriptaDecripta(texto):
    print("Encriptando", texto)
    enc= encrypt(encode(texto), e, n)
    print("Encriptação:", enc)
    dec= decode(decrypt(enc, d, n))
    print("Decriptação:", dec)


testaEncriptaDecripta("String a ser encriptada")
