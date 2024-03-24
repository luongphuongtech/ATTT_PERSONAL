import time
def GenS(key):
    T = [ord(key[i % len(key)]) for i in range(256)]
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        k = S[i]
        S[i] = S[j]
        S[j] = k
    return S

def Encyp(S, data):
    result = list()
    i = j = 0
    for para in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        r = S[i]
        S[i] = S[j]
        S[j] = r
        t = (S[i] + S[j]) % 256
        k = S[t]
        result.append(k ^ para)
        
    return bytes(result)
with open('imagetest2.jpg', 'rb') as file:
    image_data = file.read()
key = 'DAIHOCBACHKHOAHANOI'
S = GenS(key)
start_time2 = time.time()
encrypted_image_data = Encyp(S, image_data)
end_time2 = time.time()
S = GenS(key)
start_time1 = time.time()
decrypted_image_data = Encyp(S, encrypted_image_data)
end_time1 = time.time()
with open('decrypted_image.jpg', 'wb') as file:
    file.write(decrypted_image_data)
execution_time1 = end_time1 - start_time1
execution_time2 = end_time2 - start_time2
print("Thời gian thực hiện mã hóa: {:.5f} giây".format(execution_time2))
print("Thời gian thực hiện giải hóa: {:.5f} giây".format(execution_time1))