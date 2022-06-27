from Crypto.Cipher import AES

input_text = input("暗号化したい文字列を入力してください : ")

text = input_text.encode("utf-8")
nonce = bytes.fromhex("0011223344556677")

key = bytes.fromhex("00112233445566778899aabbccddeeff")
# print("key = " + str(key))

encipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

print("text = " + str(text))
encrypt_text = encipher.encrypt(text)
print("encrypt_text = " + str(encrypt_text))

decipher =  AES.new(key=key, mode=AES.MODE_CTR , nonce=nonce)
decrypt_text = decipher.decrypt(encrypt_text)
print("decrypt_text = " + str(decrypt_text))
print("decrypt_text = " + str(decrypt_text.decode("utf-8")))