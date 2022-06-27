from Crypto.Cipher import AES

input_text = input("暗号化したい文字列を入力してください : ")
text = input_text.encode("utf-8")

nonce = bytes.fromhex("1111111111111111") # 16桁
key = bytes.fromhex("11111111111111111111111111111111") # 32桁

encipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

print("text = " + str(text))
encrypt_text = encipher.encrypt(text)
print("encrypt_text = " + str(encrypt_text))

decipher =  AES.new(key=key, mode=AES.MODE_CTR , nonce=nonce)
decrypt_text = decipher.decrypt(encrypt_text)
print("decrypt_text = " + str(decrypt_text))
print("decrypt_text = " + str(decrypt_text.decode("utf-8")))