from shifercipher.shifr_cipher import ShiferCipher
from shiferaphine.shifer_aphine import Affine

shifer_cipher = ShiferCipher()
shifer_cipher_key = int(open("shifercipher/shift_cipher_key.txt").read())
shifer_cipher_encrypt = open("shifercipher/shift_cipher_message_plain.txt").read()
shifer_cipher_decrypt = open("shifercipher/shift_cipher_message_encrypt.txt").read()

result_shifer_cipher_encrypt = shifer_cipher.encryptCaesar(shifer_cipher_encrypt, shifer_cipher_key)
result_shifer_cipher_decrypt = shifer_cipher.decryptCaesar(shifer_cipher_decrypt, shifer_cipher_key)

with open("shifercipher/shift_cipher_out_message_encrypt.txt", "w") as file:
    file.write(result_shifer_cipher_encrypt)

with open("shifercipher/shift_cipher_out_message_plain.txt", "w") as file:
    file.write(result_shifer_cipher_decrypt)

affine = Affine()
affine_cipher_key = tuple(map(int, open("shiferaphine/key.txt").read().split()))
affine_cipher_encrypt = open("shiferaphine/input_plain.txt").read()
affine_cipher_decrypt = open("shiferaphine/input_encrypt.txt").read()

result_shifer_cipher_encrypt = affine.encrypt(affine_cipher_encrypt, affine_cipher_key)
result_shifer_cipher_decrypt = affine.decrypt(affine_cipher_decrypt, affine_cipher_key)

with open("shiferaphine/out_encrypt.txt", "w") as file:
    file.write(result_shifer_cipher_encrypt)

with open("shiferaphine/out_plain.txt", "w") as file:
    file.write(result_shifer_cipher_decrypt)
