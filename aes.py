from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

text = b'This is a test'

key = get_random_bytes(16)
print("key = " + str(key))

cipher = AES.new(key, AES.MODE_EAX)

print("text = " + str(text))
chipher_text, tag = cipher.encrypt_and_digest(text)
print("chipher_text = " + str(chipher_text))
print("tag = " + str(tag))

