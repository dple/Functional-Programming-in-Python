def ceasar_cipher(plain):
    in_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    out = 'XYZABCDEFGHIJKLMNOPQRSTUVWxyzabcdefghijklmnopqrstuvw '
    return ''.join(map(lambda x: out[in_.index(x)], plain))

if __name__ == '__main__':
    s = 'This is a plain message'
    cipher = ceasar_cipher(s)
    print(cipher)
