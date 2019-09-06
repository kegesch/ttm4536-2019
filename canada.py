from Crypto import Random
from Crypto.Cipher import AES
import multiprocessing

ciphertext = "6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11".decode('hex')
iv = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
keyfound = "000000307e30304d30303030b8303030"
keyfound2 = "1b860030003030003030303097303030'"

def decrypt(key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.decrypt(ciphertext)
    return result

def tryCombination(i, j, k, l, m, n):
    #print((i, j, k, l, m, n))
    # key of form xxx0x00x0000x000
    key = bytes(chr(i) + chr(j) + chr(k) + "\x00" + chr(l) + "\x00\x00" + chr(m) + "\x00\x00\x00\x00" + chr(n) + "\x00\x00\x00")
    result = str(decrypt(key))
    if "ttm4536" in result:
        print(result)
        print("key: ", key.encode("hex"))
        return True
    return False


def brute(ciphertext):
    for i in range(256):
        for j in range(256):
            for k in range(256):
                key = bytes((chr(i)+chr(j)+chr(k)).ljust(16, "\x00")).encode('hex')
                print key
                cipher = AES.new(key, AES.MODE_CBC, iv)
                result = cipher.decrypt(ciphertext)
                print result
                if "ttm4536" in result:
                    print result
                    print "key " + key.encode('hex')
                    return

def part_brute(part, start):
    print "Starting part at " + str(start * part) + " until " + str((start+1) * part)
    for i in reversed(range(256)):
        for j in range(start * part, (start+1) * part):
            for k in range(256):
                for l in range(256):
                    for m in range(256):
                        for n in range(256):
                            tryCombination(j, k, l, m, n, i)





def bruteDevide(num):
    if 256 % num != 0:
        print "num must be multiple of two"
        return
    part_per_process = 256 / num
    print "Splitting into " + str(num) + " proccesse each " + str(part_per_process) + " parts"
    for i in range(num):
        p = multiprocessing.Process(target=part_brute, args=(part_per_process, i))
        #part_brute(part_per_process, i)
        p.start()



def check():
    plaintext = "ttm4536{YouAndI}"
    key = "".join([Random.get_random_bytes(1), Random.get_random_bytes(1), Random.get_random_bytes(1)]).ljust(16,"\x00")
    keyHex = key.encode("hex")
    print keyHex
    cipher = AES.new(keyHex, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext).encode('hex')
    print ciphertext
    brute(ciphertext)
    print keyHex

bruteDevide(4)
