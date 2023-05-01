######## gitlab.bandit.B306
import tempfile
tempfile.mktemp()

############# gitlab.bandit.B413
import Crypto.Cipher
import Crypto.Random

cipher = Crypto.Cipher.AES.new('This is a key123', Crypto.Cipher.AES.MODE_CBC, 'This is an IV456')

from Crypto.Hash import SHA256

hash_object = SHA256.new(data=b'The quick brown fox jumps over the lazy dog')

import Crypto.PublicKey.RSA

key = Crypto.PublicKey.RSA.generate(2048)
