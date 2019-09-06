from Crypto.Cipher import AES


ciphertext = "6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11".decode('hex')
iv = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"


def decrypt(key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.decrypt(ciphertext)
    return result


print(decrypt("4e420000000000050000000000000000".decode('hex')))
