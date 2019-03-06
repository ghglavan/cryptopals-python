from base64 import b64encode
from binascii import unhexlify

def encode64(s):
    return b64encode(unhexlify(s)).decode('utf-8')

if __name__ == "__main__":
    s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_encoded_s = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    assert encode64(s) == expected_encoded_s