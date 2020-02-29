import string

def encrypt(plaintext, key):
    ret = ""
    for i in range(len(plaintext)):
        if plaintext[i] == "\n":
            ret += "\n"
        else:
            ret += key[ plaintext[i] ]

    return ret

def create_enc_key(multiplier, offset):
    char_arr = []
    str_chars = ""
    for c in range (32, 127):
        str_chars += chr(c)

    for i in range(len(str_chars)):
        char_arr.append(str_chars[i])

    key = []

    for i in range(len(char_arr)):
        j = (multiplier * (i + offset)) % len(str_chars)
        key[ char_arr[i] ] = char_arr[j]

    print(key)
    return key


def create_dec_key(multiplier, offset):
    #print("I am in create_enc_key()")
    char_arr = []
    str_chars = ""
    for c in range (32, 127):
        #print(c, chr(c))
        str_chars += chr(c)
    #str_chars = string.ascii_letters + string.digits + string.punctuation + ' '
    #print(str_chars)
    #print(len(str_chars)) #should equal 95
    for i in range(len(str_chars)):
        char_arr.append(str_chars[i])
    #print(char_arr)
    key = {} #dict or map array
    #calculate the modular multiplicative inverse
    inverse = 0
    while ((inverse * multiplier) % len(str_chars)) != 1:
        inverse += 1


    for i in range(len(char_arr)):
        j = ((inverse) * (i - offset)) % len(str_chars)
        key[ char_arr[i] ] = char_arr[j]
    print(key)
    return key


if __name__ == "__main__":
    print("main called from task1_lib.py")
