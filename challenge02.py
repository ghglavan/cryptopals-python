from binascii import unhexlify, hexlify

def fixed_xor(s1, s2, unhex = False):
    if unhex:
        s1 = unhexlify(s1)
        s2 = unhexlify(s2)
    
    return ''.join('{:02x}'.format(x) for x in[a1 ^ a2 for a1,a2 in zip(s1, s2)])

if __name__ == "__main__":
    s1 = '1c0111001f010100061a024b53535009181c'
    s2 = '686974207468652062756c6c277320657965'

    expected = '746865206b696420646f6e277420706c6179'

    assert fixed_xor(s1, s2, unhex=True) == expected
    assert fixed_xor(unhexlify(s1), unhexlify(s2)) == expected
     