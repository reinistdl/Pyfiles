import hashlib
md5 = hashlib.md5()
sha1 = hashlib.sha1()
toEncrypt = "Reinis Vate"
md5.update(toEncrypt.encode('utf-8'))
sha1.update(toEncrypt.encode('utf-8'))
print("\"" + toEncrypt+ "\"" + " Encrypted to MD5 (hexa): " + str(md5.hexdigest()))
print("\"" + toEncrypt+ "\"" + " Encrypted to SHA1(hexa): " + str(sha1.hexdigest()))
