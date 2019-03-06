from challenge02 import fixed_xor
from binascii import unhexlify

__letter_frequency = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
     #extra : :D,
    ' ': 0.13001,
    '\'': 0.0099,
    '.': 0.0031,
    '!': 0.0022,
    '?': 0.0011,
}

def score(s):
    sum = 0.0
    for l in s:
        if l in __letter_frequency:
            sum += __letter_frequency[l]
    return sum

def hexstr_to_str(h_s):
    return "".join([chr(x).lower() for x in unhexlify(h_s)])

def decode(s):
    scores = []

    for k in range(256):
        key = chr(k) * len(s)
        decrypted = fixed_xor(key.encode("utf-8"), unhexlify(s))
        decrypted_str = hexstr_to_str(decrypted)
        scores.append((score(decrypted_str), decrypted_str, decrypted, key))

    best = max(scores)
    return best

if __name__ == "__main__":
    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(decode(s))