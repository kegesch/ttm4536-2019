# coding: utf-8

from Crypto.PublicKey import RSA
from os import listdir
from itertools import combinations
from Crypto.Cipher import AES, PKCS1_OAEP

path = "/Users/jonas/Desktop/hackin/"

file_in_1 = path + "file1"
file_in_2 = path + "file2"

def GCD(x, y):
    while (y):
        x, y = y, x % y

    return x

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def generateprivatekey(p, q, e):
    n = p * q
    phi = (p-1) * (q-1)
    d = modinv(e, phi)
    return RSA.construct((n, e, d))

def brute():
    publicKeys = listdir(path+"file3/")
    pairsOfKeys = combinations(publicKeys, 2)
    for (x, y) in pairsOfKeys:
        public_key_x = RSA.importKey(open(path + "file3/" + x).read())
        public_key_y = RSA.importKey(open(path + "file3/" + y).read())
        keyXN = public_key_x.n
        keyXE = public_key_x.e
        keyYN = public_key_y.n
        keyYE = public_key_y.e

        gcd = GCD(keyXN, keyYN)
        if gcd != 1:
            print("Trying " + x + " and " + y)
            qX = keyXN / gcd
            print("private for " + x)
            private_x = generateprivatekey(gcd, qX, keyXE)
            assert(private_x.publickey().n == public_key_x.n)
            assert(private_x.publickey().e == public_key_x.e)
            file_out = open(path+"X.pem", "wb")
            file_out.write(private_x.exportKey())
            qY = keyYN / gcd
            print("private for " + y)
            private_y = generateprivatekey(gcd, qY, keyYE)
            assert(private_y.publickey().n == public_key_y.n)
            assert(private_y.publickey().e == public_key_y.e)
            file_out = open(path + "Y.pem", "wb")
            file_out.write(private_y.exportKey())

def decrypt(file):
    keys = [path + "X.pem", path + "Y.pem"]
    i = 0
    for k in keys:
        i += 1
        file_in = open(file, "rb")
        private_key = RSA.importKey(open(k).read())
        try:
            print("File " + file + " with Key " + k)
            data = private_key.decrypt(file_in.read())
            save = open(file + "_decrypted_" + str(i) + ".txt", "wb")
            save.write(data.decode("utf-8"))
        except UnicodeDecodeError:
            print("Could not decrypt to utf8");
        except ValueError:
            print("Could not decrypt because the message is to large")

brute()
decrypt(file_in_1)
decrypt(file_in_2)