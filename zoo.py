def to_dec(bin_str):
    temp = bin_str[::-1]
    temp = sum(int(temp[i]) * 2 ** i for i in range(len(temp)))
    return temp - 1


alpb_string = 'абвгдеёжзийклмнопрстуфxцчшщъыьэюя'

with open('ciphertext.txt', 'r') as cipher_file:
    cipher_data = [line.strip() for line in cipher_file]
decipher_data = {}

for j in range(len(cipher_data)):
    temp = list(to_dec(cipher_data[j][i * 6:(i + 1) * 6]) for i in range(len(cipher_data[j]) // 6))
    decipher_data.update({j: ''.join(alpb_string[i + 1] for i in temp)})

print(decipher_data)
