import timeit, hashlib, sys, os
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

def encryptText(password, IV, msg):
    key = hashlib.sha256(password.encode()).digest()

    cipher = AES.new(key, AES.MODE_CBC, IV)

    padded_message = Padding.pad(msg.encode(),16)
    encrypted_message = cipher.encrypt(padded_message)

    return encrypted_message

def decryptText(password, IV, enc_msg):
    key = hashlib.sha256(password.encode()).digest()
    
    cipher = AES.new(key, AES.MODE_CBC, IV)

    decrypted_message = cipher.decrypt(enc_msg)

    return Padding.unpad(decrypted_message,16).decode()

def encryptFile(password, IV, filename):
    """ IV must be a 16 bytes string"""
    key = hashlib.sha256(password.encode()).digest()


    with open(filename, 'rb') as f:
        file_data = f.read()
    starttime = timeit.default_timer()

    cipher = AES.new(key, AES.MODE_CBC, IV)
    padded_file_data = Padding.pad(file_data,16)
    encrypted_file_data = cipher.encrypt(padded_file_data)

    time = timeit.default_timer() - starttime

    with open(filename,'wb') as ef:
        ef.write(encrypted_file_data)
    return 'Done! in ' + str(time) + ' second(s)'

def decryptFile(password, IV, enc_filename):
    """ IV must be a 16 bytes string"""
    key = hashlib.sha256(password.encode()).digest()

    with open(enc_filename, 'rb') as ef:
        enc_file_data = ef.read()

    starttime = timeit.default_timer()

    cipher = AES.new(key, AES.MODE_CBC, IV)
    dec_file_data = cipher.decrypt(enc_file_data)
    file_data = Padding.unpad(dec_file_data,16)

    time = timeit.default_timer() - starttime

    with open(enc_filename,'wb') as df:
        df.write(file_data)
    return 'Done! in ' + str(time) + ' second(s)'

if sys.argv[1] == '-eF':
    print(encryptFile(sys.argv[2],b'P0123as235a145df',sys.argv[3]))
elif sys.argv[1] == '-dF':
    print(decryptFile(sys.argv[2],b'P0123as235a145df',sys.argv[3]))
elif sys.argv[1] == '-eT':
    print(encryptText(sys.argv[2],b'P0123as235a145df',sys.argv[3]))
elif sys.argv[1] == '-dT':
    print(decryptText(sys.argv[2],b'P0123as235a145df',sys.argv[3]))
else:
    print('Paramètre incorect!')